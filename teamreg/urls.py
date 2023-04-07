from django.urls import path

from .views import index, create_team, enter, inteam

app_name = 'teamreg'
urlpatterns = [
    path('', index, name='index'),
    path('create/', create_team, name='create'),
    path('join/', enter, name='join'),
    path('inteam/', inteam, name='inteam')
]
