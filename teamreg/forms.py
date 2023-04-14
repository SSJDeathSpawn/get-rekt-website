from django import forms
from .models import Team, Student, Game
import re
from userext.pullcsv import check
from functools import partial


class TeamForm(forms.ModelForm):
    def clean(self):
        if Team.objects.filter(
            name=self.cleaned_data["name"], game=self.cleaned_data["game"]
        ):
            raise forms.ValidationError("Team name already exists!")
        if Team.objects.filter(
            leader=self.cleaned_data["leader"], game=self.cleaned_data["game"]
        ):
            raise forms.ValidationError("You already have a team for this game")

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "mt-2 block text-xl rounded-sm p-2 text-white ring-4 ring-yellow-300 bg-transparent focus-visible:outline-none"
            }
        )
    )
    game = forms.ModelChoiceField(
        queryset=Game.objects.all(),
        widget=forms.RadioSelect(attrs={"class": "text-white"}),
    )
    leader = forms.HiddenInput()

    class Meta:
        model = Team
        fields = ("name", "game", "leader")


class AddMemberForm(forms.ModelForm):
    regno = forms.CharField(
        label="Registration Number",
        max_length=9,
        widget=forms.TextInput(
            attrs={
                "class": "mt-2 block text-xl rounded-sm p-2 text-white ring-4 ring-yellow-300 bg-transparent focus-visible:outline-none"
            }
        ),
    )
    team = forms.ModelChoiceField(
        queryset=Team.objects.all(),
        widget=forms.RadioSelect(attrs={"class": "text-white"}),
    )
    name = forms.CharField(
        label="Name",
        widget=forms.TextInput(
            attrs={
                "class": "mt-1 block text-xl rounded-sm p-2 text-white ring-4 ring-yellow-300 bg-transparent focus-visible:outline-none"
            }
        ),
    )
    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(
            attrs={
                "class": "mt-1 block text-xl rounded-sm p-2 text-white ring-4 ring-yellow-300 bg-transparent focus-visible:outline-none"
            }
        ),
    )
    phone = forms.IntegerField(
        label="Phone No",
        widget=forms.NumberInput(
            attrs={
                "class": "mt-1 block text-xl rounded-sm p-2 text-white ring-4 ring-yellow-300 bg-transparent focus-visible:outline-none"
            }
        ),
    )
    discordid = forms.CharField(
        label="Discord ID",
        widget=forms.TextInput(
            attrs={
                "class": "mt-1 block text-xl rounded-sm p-2 text-white ring-4 ring-yellow-300 bg-transparent focus-visible:outline-none"
            }
        ),
    )

    class Meta:
        model = Student
        fields = "__all__"

    def clean(self):
        regno = self.cleaned_data["regno"]
        regno_reg = re.compile(r"[0-9]{2}[A-Za-z]{3}[0-9]{4}")
        if regno_reg.fullmatch(regno) is None:
            raise forms.ValidationError("Not a valid registration number")
        if Student.objects.filter(
            regno=regno, team__game=self.cleaned_data["team"].game
        ):
            raise forms.ValidationError(
                "This person is already in a team for this game"
            )
