from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MyUserCreationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from .utils import generate_otp, MailSender


def signup(request):
    form = MyUserCreationForm()
    template_name = 'auth_app/signup.html'
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_url')
    return render(request, template_name, {'form': form})


def login_view(request):
    template_name = 'auth_app/login.html'
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(**data)
            if user is not None:
                otp = generate_otp()
                resp = redirect('otp_url')
                resp.set_cookie('otp', otp, max_age=120)
                resp.set_cookie('username', data.get('username'), max_age=120)
                resp.set_cookie('password', data.get('password'), max_age=120)
                subject = 'OTP Verification'
                message = f'OTP for login is {otp}'
                MailSender.send_mail(subject=subject, message=message, recipient=user.email)
                return resp
    return render(request, template_name, {'form': form})


def verify_otp(request):
    template_name = 'auth_app/otp.html'
    if request.method == 'POST':
        form_otp = request.POST.get('form_otp')
        otp = request.COOKIES.get('otp')
        if form_otp == otp:
            username = request.COOKIES.get('username')
            password = request.COOKIES.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            resp = redirect('success_url')
            resp.delete_cookie('otp')
            resp.delete_cookie('username')
            resp.delete_cookie('password')
            return resp
    return render(request, template_name)


def success_view(request):
    return HttpResponse('<h2>Login SuccessFul !!!!</h2>')


def logout_view(request):
    logout(request)
    return redirect('login_url')

