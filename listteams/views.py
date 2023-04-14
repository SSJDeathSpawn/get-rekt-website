from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from teamreg.models import Team,Student


# Create your views here.
def list_view(request):
    if(not request.user.is_staff):
        return redirect('index')

    teams = Team.objects.all()
    context={'games':{}}
    for team in teams:
        context['games'][team.name +" - "+ team.game.name]={}
        context['games'][team.name +" - "+ team.game.name]['leader']={'regno':team.leader.regno,'name':team.leader.name}
        members=list(team.members.exclude(regno=team.leader.regno))
        memberdict={}
        for i in members:
            memberdict[i.regno]=i.name
        context['games'][team.name + " - " + team.game.name]['members']=memberdict
        
    
    return render(request,"listteams.html",context)


