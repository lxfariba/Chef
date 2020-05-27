from django import forms
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from .models import Customer
from django.forms import ModelForm


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput(render_value=False), label="password")


class ProfileForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.TextInput(attrs={'size': '100'}))


class CustomerForm(forms.Form):
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(render_value=False), label="password")
    phone_number = forms.CharField(max_length=15)
    address = forms.CharField(widget=forms.TextInput(attrs={'size':'100'}))
    # order = forms.BooleanField(required=False, widget=forms.widgets.CheckboxInput(), help_text='If you want')


class ChangePasswordForm(forms.Form):
    required_css_class = 'required'

    old_password = forms.CharField(widget=forms.PasswordInput(render_value=False),
    label="Old Password")
    new_password = forms.CharField(widget=forms.PasswordInput(render_value=False),
    label="New Password")
    confirm_new_password = forms.CharField(widget=forms.PasswordInput(render_value=False),
    label="Confirm New Password")

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = user

    #     self.request = kwargs.pop("request")
    #     print(self.request)
    # self.request.user = request.user

    def clean_old_password(self):
        user = authenticate(username=self.user.username, password=self.cleaned_data['old_password'])
        if not user:
            raise forms.ValidationError('your password is not correct')
        return self.cleaned_data['old_password']

    def clean_confirm_new_password(self):
        if self.cleaned_data['confirm_new_password'] != self.cleaned_data['new_password']:
            raise forms.ValidationError("your new password doesn't match!")
        return self.cleaned_data['confirm_new_password']


class ResetPasswordForm(forms.Form):
    email = forms.CharField(max_length=500)