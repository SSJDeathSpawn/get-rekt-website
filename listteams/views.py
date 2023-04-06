from django.shortcuts import render
from django.http import HttpResponse
from teamreg.models import Team,Entry


def ListTeamsView(request):
    if(request.user.is_staff):
        context={}
        teams={}
        for group in Team.objects.all():
            members=Entry.objects.filter(team=group)
            teams[group]=[i.user.name for i in members.filter(leader=True)]+[i.user.name for i in members.exclude(leader=True)]
        context['teams']=teams
        return render(request,'listteams.html',context)

    else:
        return HttpResponse('Fail')

# Create your views here.
