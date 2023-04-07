from django.forms import ModelForm
from .models import Team, Entry


class TeamForm(ModelForm):
    class Meta:
        model = Team
        fields = ('name', 'game')

class EntryForm(ModelForm):

    def __init__(self, *args, **kwargs):
        self._user = kwargs.pop('user')
        super(EntryForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        inst = super(EntryForm, self).save(commit=False)
        inst.user = self._user
        if commit:
            inst.save()
            self.save_m2m()
        return inst

    class Meta:
        model = Entry
        exclude = ('user', 'leader')
