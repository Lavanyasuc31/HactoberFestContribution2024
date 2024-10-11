from django import forms
from .models import Profile
from django.forms import ModelForm

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name', 
            'image', 
            'age', 
            'phone_number', 
            'preferred_job_title', 
            'preferred_job_type', 
            'preferred_job_location'
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Leave blank to set username as default', 
                'class': 'form-control'
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
            'age': forms.NumberInput(attrs={
                'placeholder': 'Enter your age (optional)', 
                'class': 'form-control'
            }),
            'phone_number': forms.TextInput(attrs={
                'placeholder': 'Enter your phone number', 
                'class': 'form-control'
            }),
            'preferred_job_title': forms.Select(attrs={             
                'class': 'form-control'
            }),
            'preferred_job_type': forms.Select(attrs={
                'class': 'form-control'
            }),
            'preferred_job_location': forms.TextInput(attrs={
                'placeholder': 'Preferred job location', 
                'class': 'form-control'
            }),
        }

