from datetime import timedelta

from django import forms
from django.utils import timezone


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
