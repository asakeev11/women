from .celery import app
from django.core.mail import send_mail


@app.task
def send_email():
    subject = 'TEST TEST TEST TEST'
    message = '01010101010101'
    email_from = 'talgat.test198@gmail.com'
    recipient_list = ['talgat.asakeev@gmail.com',]
    send_mail(subject, message, email_from, recipient_list)
