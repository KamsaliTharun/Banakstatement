from django import forms
from app.models import *

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password','email','user_type']
        widgets={'password':forms.PasswordInput}