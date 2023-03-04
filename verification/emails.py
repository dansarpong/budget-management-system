from django.core.mail import send_mail
import random
from django.conf import settings
from .models import User
import smtplib , ssl


def send_otp_via_email(email):
    # subject = 'Your account verification mail.'
    otp = random.randint(1000,9999)
    message = f'Your otp is {otp}'
    # email_from = settings.EMAIL_HOST
    # send_mail(subject, message, email_from, [email])
    # print("Successfully sent email")
    smtp_server = "smtp.gmail.com"
    port = 465
    sE="adufulseth@gmail.com"
    pS="@aD611624"
    rE = [email]
    context =ssl.create_default_context()
    server =smtplib.SMTP_SSL("smtp.gmail.com",port,context=context)
    server.login(sE,pS)
    server.sendmail(sE,rE,"first message")
    user_obj = User.objects.get(email = email)
    user_obj.otp = otp
    user_obj.save()