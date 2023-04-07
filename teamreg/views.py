from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import EntryForm, TeamForm
from .models import Entry


def index(request):
    return HttpResponse('Test')

@login_required(login_url='/user/login')
def enter(request):
    if Entry.objects.filter(user__regno=request.user.regno):
        return redirect("teamreg:inteam")
    else:
        print(f"{request.user.regno} is not in any event")
        print(Entry.objects.filter(user__regno=request.user.regno))
    if request.method == 'POST':
        form = EntryForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('teamreg:index')
    form = EntryForm(user=request.user)
    context = {
        'form': form,
        'request': request
    }
    return render(request, 'jointeam.html', context)


@login_required(login_url='/user/login')
def create_team(request):
    if Entry.objects.filter(user__regno=request.user.regno):
        return redirect("teamreg:inteam")
    else:
        print(f"{request.user.regno} is not in any event")
        print(Entry.objects.filter(user__regno=request.user.regno))
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            team = form.save()
            entry = Entry(user=request.user, team=team, leader=True)
            entry.save()
            return redirect('teamreg:index')
    form = TeamForm()
    context = {
        'form': form,
        'request': request
    }
    return render(request, 'newteam.html', context)


def inteam(request):
    return render(request, 'inteam.html', {'request': request})
