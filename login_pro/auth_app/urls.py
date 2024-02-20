from django.urls import path
from .views import signup, login_view, success_view, verify_otp, logout_view

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login_url'),
    path('otp/', verify_otp, name='otp_url'),
    path('success/', success_view, name='success_url'),
    path('logout/', logout_view, name='logout_url'),
]
