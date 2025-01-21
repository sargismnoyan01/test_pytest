from django import forms
from .models import *

class UserFrom(forms.ModelForm):
    class Meta:
        model = UserClass
        fields = '__all__'
