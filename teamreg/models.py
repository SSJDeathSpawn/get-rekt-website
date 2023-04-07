from django.db import models
from userext.models import UserEXT


# Create your models here.

class Game(models.Model):
    short_name = models.CharField(max_length=3)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Team(models.Model):

    name = models.CharField(max_length=30)
    game = models.ManyToManyField(Game)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Entry(models.Model):
    user = models.ForeignKey(UserEXT, on_delete=models.CASCADE, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    leader = models.BooleanField(default=False)

    def __str__(self):
        return self.team.name + " - " + self.user.regno

    class Meta:
        verbose_name_plural = "entries"
