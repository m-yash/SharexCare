from django import forms
from .models import UserForm

class FormUserForm(forms.ModelForm):
    class Meta:
        model = UserForm
        fields = ["username","email","password"]