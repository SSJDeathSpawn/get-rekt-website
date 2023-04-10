from django.shortcuts import render
from django.http import HttpResponse
from teamreg.models import Team


# Create your views here.
def list_view(request):
    if(request.user.is_staff):
        context={}
        teams={}
        for group in Team.objects.all():
            members=group.members
            teams[group]=[group.leader.name]+[i.user.name for i in members]
        context['teams']=teams
        return render(request,'listteams.html',context)

    else:
        return HttpResponse('Fail')

