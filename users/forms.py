from django import forms
from .models import User
from django.core.validators import RegexValidator, ValidationError

class LoginUser(forms.Form):
    nickname = forms.CharField(max_length=15, required=True)
    password = forms.CharField(max_length=20, required=True, validators=[RegexValidator(regex='^.{8}$', message='Length has to be 8', code='nomatch')])

    widgets = {
            'nickname': forms.TextInput(attrs={'class': 'fadeIn second', 'placeholder': '닉네임'}),
            'password': forms.TextInput(
                attrs={'class': 'fadeIn third', 'placeholder': '비밀번호'}),
    }


class CreateUser(forms.Form):
    username = forms.CharField(max_length=10, required=True)
    nickname = forms.CharField(max_length=15, required=True)
    password = forms.CharField(max_length=20, required=True, validators=[RegexValidator(regex='^.{8}$', message='Length has to be 8', code='nomatch')])
    re_password = forms.CharField(max_length=20, required=True)

    widgets = {
            'username': forms.TextInput(attrs={'class': 'fadeIn second', 'placeholder': '이름'}),
            'nickname': forms.TextInput(attrs={'class': 'fadeIn second', 'placeholder': '닉네임'}),
            'password': forms.TextInput(
                attrs={'class': 'fadeIn third', 'placeholder': '사용할 비밀번호'}),
            're_password': forms.TextInput(
                attrs={'class': 'fadeIn third', 'placeholder': '비밀번호 재입력'}),
    }

    def clean_re_password(self):
        cd = self.cleaned_data

        password1 = cd.get('password')
        password2 = cd.get('re_password')

        if password1 != password2:
            raise ValidationError("Passwords did not match")

        return cd