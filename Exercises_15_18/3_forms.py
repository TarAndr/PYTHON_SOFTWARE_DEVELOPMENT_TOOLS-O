# forms.py

from django import forms
from .models import Auto

class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['brand', 'model', 'year', 'color']
