from django.forms import ModelForm, TextInput
from .models import *


class SubscribersForm(ModelForm):
    class Meta:
        model = Subscribers
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name...',

            }),
            'email': TextInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'Enter email...',

            })
        }