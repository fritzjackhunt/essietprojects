# from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader, context
from django.shortcuts import render
import json



def home(request):
    return render(request, 'essietproject/base.html')

def contacts(request):
    return render(request, 'essietproject/contacts.html')
