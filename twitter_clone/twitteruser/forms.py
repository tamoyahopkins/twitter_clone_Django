from django import forms
from django.forms import ModelForm
from twitteruser.models import MyCustomUser, Ticket
from django.contrib.auth.forms import AuthenticationForm
# from django.shortcuts import get_object_or_404, render, redirect
# from twitteruser.admin import UserAdmin


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    # password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = MyCustomUser
        fields = '__all__'
        exclude =['password','groups', 'is_superuser', 'username', 'last_login', 'user_permissions', 'is_staff', 'is_active', 'date_joined','id_password2', 'id_password1']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class AddTicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = [
            'title',
            'description',
            'assign_to_user'
        ]

class LogInForm(AuthenticationForm):
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))


class AssignTicket(forms.ModelForm):
    class Meta:
        model = Ticket
        fields =['assign_to_user']