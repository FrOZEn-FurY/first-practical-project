from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)
    email = forms.EmailField()
    firstname = forms.CharField(max_length=50)
    lastname = forms.CharField(max_length=50)
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=50)