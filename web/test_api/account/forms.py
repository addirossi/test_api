from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from rest_framework import exceptions
from rest_framework.authtoken.models import Token


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()

    def get_user_token(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(username=username, password=password)
        if not user:
            raise exceptions.AuthenticationFailed(_(
                'Username or password are incorrect'))
        token, created = Token.objects.get_or_create(user=user)

        return user, token.key

    def save(self, *args, **kwargs):
        if not self.is_valid():
            raise exceptions.ValidationError(self.errors)
        return self.get_user_token()