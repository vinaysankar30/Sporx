from django import forms


class UserForms(forms.Form):
    user_email = forms.CharField(label='email', max_length=100)
    password = forms.CharField(label='password', max_length=20)
