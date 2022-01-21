from django import forms 
from .models import Lead, Agent
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

User = get_user_model()


class Lead_Form(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['first_name', 'last_name', 'age', 'agent', 'organization']


class Lead_Edit_Form(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['first_name', 'last_name', 'age', 'agent', 'organization']


class CustomUser(UserCreationForm):
    class Meta:
        model = User 
        fields = ("username",)
        field_classes = {"username": UsernameField}