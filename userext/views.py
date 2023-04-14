from django.shortcuts import render, redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth import login as login_user,authenticate,logout as logout_user
from .pullcsv import name
from teamreg.models import Student


def register(request):
    context={}
    if (request.POST):
        
        
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            regno=form.cleaned_data.get('regno')
            raw_password=form.cleaned_data.get('password1')
            account=authenticate(regno=regno,password=raw_password)
            login_user(request,account)
            s=Student(regno=regno,name=form.cleaned_data.get('name'),email=form.cleaned_data.get('email'),phone=form.cleaned_data.get('phone'),discordid=form.cleaned_data.get('discord'))
            s.save()
            return redirect('userext:index')
        else:
            form.fields.pop('name')
            context['form']=form
    else:
        form=RegisterForm()
        context['form']=form
    return render(request,'register.html',context)

def index(request):
    return redirect('index')

def logout(request):
    logout_user(request)
    return redirect('userext:index')

def login(request):
    context={}
    user=request.user
    if (user.is_authenticated):
        return redirect("userext:index")
    if request.POST:
        form=LoginForm(request.POST)
        if (form.is_valid()):
            regno=request.POST['regno']
            password=request.POST['password']
            user=authenticate(regno=regno,password=password)
            login_user(request,user)
            return redirect('userext:index')
    
    else:
        form=LoginForm()

    context['form']=form
    return render(request,'login.html',context)
