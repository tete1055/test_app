from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms

class CustomUserCreationForm(UserCreationForm):
    '''
    '''
    class Meta:
        '''

        Attributes:
          model:
          fields:
        '''
        model = CustomUser
        fields = ('image', 'username', 'email', 'password1', 'password2')