from django.urls import path

from .views import index, create_team, add_members,view_members

app_name = 'teamreg'
urlpatterns = [
    path('', index, name='index'),
    path('create/', create_team, name='create'),
    path('add/', add_members, name='add'),
    path('list/',view_members,name='view')
]
