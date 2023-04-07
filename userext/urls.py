from django.urls import path

from .views import login, index, register, logout
 
app_name = 'userext'
urlpatterns = [
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]
