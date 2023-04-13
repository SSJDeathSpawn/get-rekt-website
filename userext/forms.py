from django import forms
from .models import UserEXT
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from .pullcsv import check
import re

class RegisterForm(UserCreationForm):
    field_order = ["regno", "password1", "password2", "name"]

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "mt-1 block text-xl rounded-sm p-2 text-white ring-4 ring-cyan-300 bg-transparent focus-visible:outline-none"
            }
        ),
    )
    password2 = forms.CharField(
        label="Password Confirmation",
        widget=forms.PasswordInput(
            attrs={
                "class": "mt-1 block text-xl rounded-sm p-2 text-white ring-4 ring-cyan-300 bg-transparent focus-visible:outline-none"
            }
        ),
        help_text="Enter the same password as above, for verification.",
    )

    class Meta:
        model = UserEXT
        fields = ("regno", "password1", "password2", "name")
        widgets = {
            "regno": forms.TextInput(
                attrs={
                    "class": "mt-1 block text-xl rounded-sm p-2 text-white ring-4 ring-cyan-300 bg-transparent focus-visible:outline-none"
                }
            ),
        }
        labels = {"password": "Password", "regno": "Registration Number"}

    def clean(self):
        regno = self.cleaned_data["regno"]
        regno_reg = re.compile(r"[0-9]{2}[A-Za-z]{3}[0-9]{4}")
        if regno_reg.fullmatch(regno) is None:
            raise forms.ValidationError("Not a valid registration number")
        if not check(regno):
            raise forms.ValidationError("Not a TAG Club Member")
        


class LoginForm(forms.ModelForm):
    class Meta:
        model = UserEXT
        fields = ("regno", "password")
        widgets = {
            "regno": forms.TextInput(
                attrs={
                    "class": "mt-2 block text-xl rounded-sm p-2 text-white ring-4 ring-green-400 bg-transparent focus-visible:outline-none"
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "class": "mt-2 block text-xl rounded-sm p-2 text-white ring-4 ring-green-400 bg-transparent focus-visible:outline-none"
                }
            ),
        }
        labels = {"password": "Password", "regno": "Registration Number"}

    def clean(self):
        regno = self.cleaned_data["regno"]
        password = self.cleaned_data["password"]
        if not (authenticate(regno=regno, password=password)):
            raise forms.ValidationError("Invalid RegNo/Password")
