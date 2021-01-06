# from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader, context
from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from .models import Subscribe
from .utils import SendSubscribeMail
from marketing.forms import EmailSignupForm
from marketing.models import Signup
from django.core.mail import send_mail



def home(request):
    return render(request, 'essietproject/home.html')

def contacts(request):
    if request.method == "POST":
        contact_fname = request.POST['fname']
        contact_lname = request.POST['lname']
        contact_email = request.POST['email']
        contact_message = request.POST['message']

        send_mail(
            contact_fname, 
            contact_message,
            contact_email,
            ['essiet.aniekan31@gmail.com'],
            fail_silently = False,
        )


        return render(request, 'essietproject/contacts.html', {'contact_fname' : contact_fname})


    else:
        return render(request, 'essietproject/contacts.html')


def aboutus(request):
    return render(request, 'essietproject/company/aboutus.html')
