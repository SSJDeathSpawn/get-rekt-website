from django.urls import path

from .views import list_view

app_name = 'listteams'
urlpatterns = [
    path('', list_view, name='list')
]
