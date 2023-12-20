from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from django.contrib import messages
from .forms import UserRegisterForm, UpdateUserInfoForm

def usershow(request):
    objs = models.register.objects.all()
    info = {"objs" : objs, 'cnt':1,}
    return render(request, 'users.html', info)
def homemessage(request):
    info = {'name' : 'hossein', 'nums' : [1,2,3,4,5,6,7,8,9,10]}
    return render(request, 'home.html', info)
def defaultmessage(request):
    return HttpResponse('hello, this is the default page')
def getid(request, id):
    obj = models.register.objects.get(id=id)
    s = {'info':obj}
    return render(request,'user.html',s)
def deleteobj(request, id):
    obj = models.register.objects.get(id=id)
    obj.delete()
    messages.success(request,message="Your user had been deleted successfully")
    return redirect('users')
def registerform(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            models.register.objects.create(firstname=cd['firstname'], lastname=cd['lastname'], email=cd['email'])
            return redirect('users')
    else:    
        form = UserRegisterForm()
    return render(request,'reg.html',{'form':form})
def Update(request, id):
    user = models.register.objects.get(id=id)
    if request.method == 'POST':
        form = UpdateUserInfoForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your info has been updated succesfully')
            return redirect('user',id)
    else:
        form = UpdateUserInfoForm(instance=user)
    return render(request,'update.html',{'form':form})    