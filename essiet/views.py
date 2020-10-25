# from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader, context
from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from .models import Subscribe
from .utils import SendSubscribeMail



def home(request):
    return render(request, 'essietproject/base.html')

def contacts(request):
    return render(request, 'essietproject/contacts.html')





def subscribe(request):
    if request.method == 'POST':
        email = request.POST['email_id']
        email_qs = Subscribe.objects.filter(email_id = email)
        if email_qs.exists():
            data = {"status" : "404"}
            return JsonResponse(data)
        else:
            Subscribe.objects.create(email_id = email)
            SendSubscribeMail(email) # Send the Mail, Class available in utils.py
            
    return HttpResponse("/")

