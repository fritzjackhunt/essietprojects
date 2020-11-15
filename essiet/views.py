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




def home(request):
    return render(request, 'essietproject/base.html')

def contacts(request):
    return render(request, 'essietproject/contacts.html')

def aboutus(request):
    return render(request, 'essietproject/company/aboutus.html')