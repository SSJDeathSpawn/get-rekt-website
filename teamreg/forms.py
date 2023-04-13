from django import forms
from .models import Team, Student, Game
import re
from userext.pullcsv import check
from functools import partial


class TeamForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self._leader = kwargs.pop("leader")
        super(TeamForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(TeamForm, self).save(commit=False)
        inst.leader = self._leader
        if commit:
            inst.save()
            self.save_m2m()
        return inst

    def clean(self):
        if Team.objects.filter(name=self.cleaned_data['name']):
            print("Should error!")
            raise forms.ValidationError("Team name already exists!")

    name = forms.CharField(widget=forms.TextInput(attrs={"class": "mt-2 block text-xl rounded-sm p-2 text-white ring-4 ring-green-400 bg-transparent focus-visible:outline-none"}))
    game = forms.ModelMultipleChoiceField(queryset=Game.objects.all(), widget=forms.CheckboxSelectMultiple(attrs={'class': 'text-white'}))

    class Meta:
        model = Team
        fields = ("name", "game")
        # widgets = {
        #         'game' : forms.CheckboxSelectMultiple(attrs={'class': 'text-white'})
        # }


class AddMemberForm(forms.Form):
    regno = forms.CharField(max_length=9, widget=forms.TextInput(attrs={"class": "mt-2 block text-xl rounded-sm p-2 text-white ring-4 ring-green-400 bg-transparent focus-visible:outline-none"}))

    def __init__(self, *args, **kwargs):
        self.team = kwargs.pop("team")
        super(AddMemberForm, self).__init__(*args, **kwargs)
    


    def clean_regno(self):
        regno = self.cleaned_data["regno"]
        regno_reg = re.compile(r"[0-9]{2}[A-Za-z]{3}[0-9]{4}")
        if regno_reg.fullmatch(regno) is None:
            raise forms.ValidationError("Not a valid registration number")
        if not check(regno):
            raise forms.ValidationError("Not a TAG Club Member")
        

        return regno
