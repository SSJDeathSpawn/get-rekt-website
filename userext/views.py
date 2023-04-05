from django.shortcuts import render, redirect
from .forms import RegisterForm,LoginForm
from django.contrib.auth import login,authenticate,logout
from .pullcsv import name


def RegisterView(request):
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
            login(request,account)
            return redirect('temp')
        else:
            form.fields.pop('name')
            context['registration_form']=form
    else:
        form=RegisterForm()
        form.fields.pop('name')
        context['registration_form']=form
    return render(request,'register.html',context)

def tempview(request):
    context={}
    return render(request,'temp.html',context)

def LogOutView(request):
    logout(request)
    return redirect('temp')

def LogInView(request):
    context={}
    user=request.user
    if (user.is_authenticated):
        return redirect("temp")
    if request.POST:
        form=LoginForm(request.POST)
        if (form.is_valid()):
            regno=request.POST['regno']
            password=request.POST['password']
            user=authenticate(regno=regno,password=password)
            login(request,user)
            return redirect('temp')
    
    else:
        form=LoginForm()

    context['login_form']=form
    return render(request,'login.html',context)