from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from users.models import CustomUser


# Create your views here.
class RegisterVIEW(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, 'users/register.html', {"form": register_form})

    def post(self, request):
        register_form = RegisterForm(data=request.POST)
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'You have successfully registered.')
            return redirect("liga:home")
        else:
            return render(request, 'users/register.html', {"form": register_form})


class LoginVIEW(View):
    def get(self, request):
        login_form = AuthenticationForm()
        return render(request, 'users/login.html', {"form": login_form})

    def post(self, request):
        login_form = AuthenticationForm(data=request.POST)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            messages.success(request, "You are now logged in.")
            return redirect("liga:home")
        return render(request, 'users/login.html', {"form": login_form})


class LogoutVIEW(View):
    def get(self, request):
        logout(request)
        messages.warning(request, "You have been logged out.")
        return redirect("liga:home")


class ProfileVIEW(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("users:login")
        return render(request, 'users/profile.html', {"user": request.user})
