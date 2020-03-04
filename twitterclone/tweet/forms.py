from django import forms
from django.forms import ModelForm
from tweet.models import Tweet

class Tweet_form(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = [
            'text'
        ]
