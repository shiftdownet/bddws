from django.shortcuts import render, redirect
from django.views import generic
from .models import CustomUser
from django.views.generic.base import TemplateView
from django.views.generic.base import View
from django.contrib.auth.views import LoginView as BaseLoginView,  LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from .forms import *
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.mixins import LoginRequiredMixin
from .provider import UserData


class LoginView(BaseLoginView):
    form_class = LoginFrom
    template_name = "accounts/login.html"


class LogoutView(BaseLogoutView):
    pass


class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    form_class = SetPasswordForm
    success_url = reverse_lazy('accounts:password_change_done')
    template_name = 'accounts/password_change.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form_name"] = "password_change"
        return context


class PasswordChangeDone(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'accounts/password_change_done.html'


class ProfileView(View):
    def get(self, request, *args, **kwargs):
        if "user_id" in request.GET:
            user_id = request.GET["user_id"]
        else:
            user_id = self.request.user

        try:
            user_ctx = UserData().get(user_id, str(self.request.user) == str(user_id))
            return render(request, "accounts/profile.html", {"view": user_ctx, "yourself": (str(self.request.user) == str(user_id))})
        except:
            pass

        return render(request, "bddws/error.html", {"error": "不正なリクエストです", "detail": ""})
