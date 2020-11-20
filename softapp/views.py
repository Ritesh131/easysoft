from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from .serializers import UserQuerySerializer
from .models import UserQuery
from rest_framework import viewsets
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import get_connection, EmailMultiAlternatives


# Create your views here.

class index(TemplateView):
    template_name = 'index.html'

def QuerySubmit(req):
    if req.method == 'POST':
        name = req.POST['name']
        email = req.POST['email']
        number = req.POST['number']
        message = req.POST['message']
        userQuery = UserQuery(name=name, email=email, number=number, message=message)
        userQuery.save()
        try:
            subject = 'EasySoft Tech'
            message = 'Thank you connect with us. Our team will get back you soon.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail( subject, message, email_from, recipient_list)
        except:
            print(f'There are some err to sending email')
        return HttpResponse('Thanks For Contact. You will getback soon')