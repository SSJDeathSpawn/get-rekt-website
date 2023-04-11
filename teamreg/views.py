from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import TeamForm, AddMemberForm
from .models import Team, Student


def index(request):
    return HttpResponse("Test")


@login_required(login_url="/user/login")
def create_team(request):
    if request.method == "POST":
        form = TeamForm(request.POST, leader=request.user)
        if form.is_valid():
            team = form.save()
            team.members.add(Student.objects.filter(regno=request.user.regno).first())
            return redirect("teamreg:index")
    form = TeamForm(leader=request.user)
    context = {"form": form, "request": request}
    return render(request, "newteam.html", context)


@login_required(login_url="/user/login")
def add_members(request):
    team = Team.objects.filter(leader=request.user).first()
    if team is None:
        return HttpResponseForbidden("You must be a team leader to add members")
    if request.method == "POST":
        form = AddMemberForm(request.POST,team=team)
        if form.is_valid():
            
            team.members.add(Student.objects.filter(regno=form.cleaned_data['regno']).first())
            return redirect("teamreg:add")
        else:
           context = {"request": request, "form": form}
           return render(request, "addmembers.html", context) 
    form = AddMemberForm(team=team)
    context = {"request": request, "form": form}
    return render(request, "addmembers.html", context)


@login_required(login_url="/user/login")
def view_members(request):
    team = Team.objects.filter(leader=request.user).first()
    if team is None:
        return HttpResponseForbidden("You must be a team leader to view teams")
    if request.method=="POST":
        regno=request.POST["regno"]
        
        team.members.remove(Student.objects.get(regno=regno))
        
        return redirect("teamreg:view")
    members=list(team.members.exclude(regno=request.user.regno))
    memberdict={}
    for i in members:
        memberdict[i.regno]=i.name
    context={"leader":{"regno":request.user.regno,"name":request.user.name},"members":memberdict}
    return render(request,"viewmembers.html",context)
