from django import forms

from .models import *


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "message")