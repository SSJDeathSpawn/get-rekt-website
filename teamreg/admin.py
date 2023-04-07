from django.contrib import admin
from .models import Game, Team, Entry


# Register your models here.
admin.site.register(Team)
admin.site.register(Entry)
admin.site.register(Game)
