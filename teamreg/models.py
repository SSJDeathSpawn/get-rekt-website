from django.db import models
from userext.models import UserEXT


# Create your models here.
class Game(models.Model):
    short_name = models.CharField(max_length=3)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Student(models.Model):

    regno=models.CharField(max_length=9,primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    phone = models.IntegerField()

    class Meta:
        ordering = ['regno']

    def __str__(self):
        return self.name

class Team(models.Model):

    name = models.CharField(max_length=30, primary_key=True)
    game = models.ManyToManyField(Game)
    leader = models.ForeignKey(UserEXT, on_delete=models.CASCADE, related_name='leader')
    members = models.ManyToManyField(Student)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
