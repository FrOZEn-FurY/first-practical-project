from django import forms
from django.forms import ModelForm 
from .models import register

class UserRegisterForm(forms.Form):
    firstname = forms.CharField(max_length=100)
    lastname = forms.CharField(max_length=100)
    email = forms.EmailField() 
    
class UpdateUserInfoForm(ModelForm):
    class Meta:
        model = register
        fields = '__all__'