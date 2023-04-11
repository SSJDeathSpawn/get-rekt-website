from django import forms
from .models import Team, Student, Game
import re
from userext.pullcsv import check


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

    class Meta:
        model = Team
        fields = ("name", "game")
        widgets = {
                    'game': 
                    forms.CheckboxSelectMultiple
                }


class AddMemberForm(forms.Form):
    regno = forms.CharField(max_length=9)

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
