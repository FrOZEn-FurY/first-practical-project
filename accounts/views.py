from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from django.contrib import messages

def register_user(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'],cd['email'],cd['password'])
            user.first_name = cd['firstname']
            user.last_name = cd['lastname']
            user.save()
            messages.success(request,"you have been registered as a real user successfully")
            return redirect('users')
    return render(request,'register.html',{'form':form})    

def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request,user)
                msg = 'Welcome, ' + cd['username']
                messages.success(request,msg)
                return redirect('users')
            else:
                messages.error(request,"The user does not exist")
    return render(request,'login.html',{'form':form})   

def logout_user(request):
    msg = "The user " + request.user.username + " has been loged out successfully"
    logout(request)
    messages.success(request,msg)
    return redirect('users')   