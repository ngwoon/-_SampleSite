from django import forms
from .models import User
from django.core.validators import RegexValidator, ValidationError

class LoginUser(forms.Form):
    username = forms.CharField(max_length=15, required=True)
    password = forms.CharField(max_length=20, required=True, validators=[RegexValidator(regex='^.{8}$', message='Length has to be 8', code='nomatch')])

    widgets = {
            'username': forms.TextInput(attrs={'class': 'fadeIn second', 'placeholder': '아이디'}),
            'password': forms.TextInput(
                attrs={'class': 'fadeIn third', 'placeholder': '비밀번호'}),
    }


class CreateUser(forms.Form):
    realname = forms.CharField(max_length=10, required=True)
    username = forms.CharField(max_length=15, required=True)
    password = forms.CharField(max_length=20, required=True, validators=[RegexValidator(regex='^.{8}$', message='Length has to be 8', code='nomatch')])
    re_password = forms.CharField(max_length=20, required=True)

    widgets = {
            'realname': forms.TextInput(attrs={'class': 'fadeIn second', 'placeholder': '이름'}),
            'username': forms.TextInput(attrs={'class': 'fadeIn second', 'placeholder': '아이디'}),
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