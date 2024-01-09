from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = "accounts"
urlpatterns = [
    path("", login_required(views.ProfileView.as_view()), name="index"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("profile/", login_required(views.ProfileView.as_view()), name="profile"),
    path("password_change/", login_required(views.PasswordChange.as_view()), name="password_change"),
    path("password_change/done/", login_required(views.PasswordChangeDone.as_view()), name="password_change_done"),
]

