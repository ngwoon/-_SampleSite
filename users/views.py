from django.shortcuts import render, redirect
from .forms import LoginUser, CreateUser
from .models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def try_login(request):
    if request.method == "POST":
        form = LoginUser(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user=user)
                messages.success(request, '로그인 성공')
            else:
                messages.warning(request, '로그인 실패')

            return redirect('mysite:index')
        else:
            messages.warning(request, '잘못된 입력입니다.')
            return redirect('mysite:index')
    else:
        form = LoginUser()
        return render(request, "users/login.html", {'form': form})

def try_logout(request):
    logout(request)
    return redirect('mysite:index')

def create(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            duplicated = User.objects.filter(username=form.cleaned_data['username'])
            if duplicated:
                messages.warning(request, "이미 사용중인 아이디입니다.")
                return redirect('users:create')
            else:
                user = User.objects.create(username=form.cleaned_data['username'], realname=form.cleaned_data['realname'])
                user.set_password(form.cleaned_data['password'])
                user.save()
                return redirect('users:login')

        else:
            messages.warning(request, "잘못된 입력입니다.")
            return redirect('users:create')

    else:
        form = CreateUser()
        return render(request, "users/create.html", {'form': form})
