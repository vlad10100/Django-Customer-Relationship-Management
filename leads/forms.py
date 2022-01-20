from django import forms 
from .models import Lead, Agent


class Lead_Form(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['first_name', 'last_name', 'age', 'agent']


class Lead_Edit_Form(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['first_name', 'last_name', 'age']