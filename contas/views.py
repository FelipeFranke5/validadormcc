from typing import Any
from django.shortcuts import redirect
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import RegisterModelForm


class CustomLoginView(LoginView):
    template_name = "login.html"

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if self.request.user.is_authenticated:
            return redirect("/")
        return super().get(request, *args, **kwargs)


class CustomLogoutView(LogoutView):
    template_name = "logout.html"


class RegisterNewUser(CreateView):
    template_name = "register.html"
    model = User
    form_class = RegisterModelForm

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        if self.request.user.is_authenticated:
            return redirect("/")
        return super().get(request, *args, **kwargs)

    def get_success_url(self) -> str:
        return reverse_lazy("contas:login")
