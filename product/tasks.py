import time
from celery import shared_task , Celery
from core.models import Subscriber
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives , send_mail
from django.conf import settings

import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'multikart.settings'

@shared_task
def export_data():
    print('Process start!')
    time.sleep(10)
    print('Process End')


@shared_task
def send_email_to_subs():
    email_lists = Subscriber.objects.values_list('email' , flat=True)
    message = render_to_string('core/email-subscribers.html')
    subject = 'Best Products !'
    from_email = 'feridhuseynli13@gmail.com'
    recipient_list = email_lists
    
    send_mail(subject, message, from_email, recipient_list)

