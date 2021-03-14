# from django.shortcuts import render

from django.http import HttpResponse
from django.template import loader, context
from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse
from django.core.mail import send_mail
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Job 
from .forms import JobForm, JobEditForm
from django.urls import reverse_lazy



#def home(request):
 #   return render(request, 'essietproject/based.html')

class HomeView(ListView):
    model = Job
    template_name = 'essietproject/based.html'
    ordering = ['-id']

class JobDetailView(DetailView):
    model = Job
    template_name = 'essietproject/job_details.html'

class AddJobView(CreateView):
    model = Job
    form_class = JobForm
    template_name = 'essietproject/post_job.html'
    #fields = '__all__'

class JobUpdateView(UpdateView):
    model = Job
    form_class = JobEditForm
    template_name = 'essietproject/update_job.html'
    #fields = ['title', 'description']

class JobDeleteView(DeleteView):
    model = Job
    template_name = 'essietproject/delete_job.html'
    success_url = reverse_lazy('homepage')



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
