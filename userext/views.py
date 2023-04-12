from django.shortcuts import render, redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth import login as login_user,authenticate,logout as logout_user
from .pullcsv import name


def register(request):
    context={}
    if (request.POST):
        data={'regno':request.POST['regno'],'password1':request.POST['password1'],'password2':request.POST['password2'],'name':''}
        data['name']=name(data['regno'])
        form=RegisterForm(data)
        if form.is_valid():
            form.save()
            regno=form.cleaned_data.get('regno')
            raw_password=form.cleaned_data.get('password1')
            account=authenticate(regno=regno,password=raw_password)
            login_user(request,account)
            return redirect('userext:index')
        else:
            form.fields.pop('name')
            context['registration_form']=form
    else:
        form=RegisterForm()
        form.fields.pop('name')
        context['registration_form']=form
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

    context['login_form']=form
    return render(request,'login.html',context)
