from datetime import timedelta
from django import forms
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Comment

User = get_user_model()

class Reminder(forms.Form):
    email = forms.EmailField(required=True, max_length=100)
    message = forms.CharField(required=True, max_length=300)
    time = forms.DateTimeField(required=True, initial=timezone.now())

    def clean_eta(self):
        time = self.cleaned_data['time']
        if time < timezone.now():
            raise forms.ValidationError('Wrong time')
        if time > (timezone.now() + timedelta(days=2)):
            raise forms.ValidationError('Wrong time')
        return time


class Register(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password_1', 'password_2']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['username', 'text']
