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
        form = AddMemberForm(request.POST)
        if form.is_valid():
            team.members.add(Student.objects.filter(regno=form.cleaned_data['regno']).first())
            return redirect("teamreg:add")
    form = AddMemberForm()
    context = {"request": request, "form": form}
    return render(request, "addmembers.html", context)
