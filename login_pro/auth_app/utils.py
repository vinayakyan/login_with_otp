import random
from django.core.mail import EmailMessage


def generate_otp():
    return random.randint(000000, 999999)


class MailSender:

    @staticmethod
    def send_mail(subject, message, recipient):
        email = EmailMessage(subject=subject, body=message, to=[recipient,])
        email.send()
