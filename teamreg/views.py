from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import TeamForm, AddMemberForm
from .models import Team, Student, Game

def index(request):
    return redirect('index')


@login_required(login_url="/user/login")
def create_team(request):
    if request.method == "POST":
        data={"name":request.POST["name"],"game":request.POST["game"],"leader":request.user}
        form = TeamForm(data)
        if form.is_valid():
            team = form.save()
            team.members.add(Student.objects.get(regno=request.user.regno))
            return redirect("teamreg:view")
        else:
            context = {"form": form, "request": request}
            return render(request, "newteam.html", context)
    form = TeamForm()
    form.fields.pop("leader")
    context = {"form": form, "request": request}
    
    return render(request, "newteam.html", context)


@login_required(login_url="/user/login")
def add_members(request):
    team = Team.objects.filter(leader=request.user)
    if team is None:
        return HttpResponseForbidden("You must be a team leader to add members")
    if request.method == "POST":
        form = AddMemberForm(request.POST)
        if form.is_valid():
            form.save()
            form.cleaned_data['team'].members.add(Student.objects.filter(regno=request.POST["regno"]).last()) 
            return redirect("teamreg:add")
        else:
           context = {"request": request, "form": form}
           return render(request, "addmembers.html", context) 
    form = AddMemberForm()
    team=list(i.id for i in team if i.members.count()<i.game.max)
    if(len(team)==0):
        context={"request":request,"form":None}
        return render (request,"addmembers.html",context)
    form.fields["team"].queryset=Team.objects.filter(id__in=team)
    context = {"request": request, "form": form}
    return render(request, "addmembers.html", context)


@login_required(login_url="/user/login")
def view_members(request):
    teams = Team.objects.filter(leader=request.user)
    if teams is None:
        return HttpResponseForbidden("You must be a team leader to view teams")
    if request.method=="POST":
        if 'regno' in request.POST:
            regno=request.POST['regno'].split(" ")[0]
            name=request.POST['regno'].split(" - ")[-1]
            teams.get(game=Game.objects.get(name=name)).members.get(regno=regno).delete()
            
            return redirect("teamreg:view")
        elif 'team' in request.POST:
            team = ' - '.join(request.POST['team'].split(' - ')[:-1])
            teams.get(name=team).delete()
            return redirect("teamreg:view")
    context={'games':{}}
    for team in teams:
        context['games'][team.name +" - "+ team.game.name]={}
        context['games'][team.name +" - "+ team.game.name]['leader']={'regno':request.user.regno,'name':request.user.name}
        members=list(team.members.exclude(regno=request.user.regno))
        memberdict={}
        for i in members:
            memberdict[i.regno]=i.name
        context['games'][team.name + " - " + team.game.name]['members']=memberdict
        
    
    return render(request,"viewmembers.html",context)
