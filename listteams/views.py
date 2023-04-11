from django.shortcuts import render
from django.http import HttpResponse
from teamreg.models import Team,Student


# Create your views here.
def list_view(request):
    if(request.user.is_staff):
        context={}
        teams={}
        for group in Team.objects.all():
            members=group.members.exclude(regno=group.leader)
            leader=Student.objects.filter(regno=group.leader)[0]
            teams[group]=[leader.regno+" : "+leader.name]+list(i.regno+" : "+i.name for i in members)
        context['teams']=teams
        return render(request,'listteams.html',context)

    else:
        return HttpResponse('Fail')

