from django.contrib import admin
from .models import Game, Team, Student


# Register your models here.
admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Student)
