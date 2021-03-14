from django import forms
from .models import Job

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'author', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Describe your job here!"}),

        }

class JobEditForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title', 'description')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control',}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': "Describe your job here!"}),
            
        }