from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path("", views.ProfileView.as_view(), name="index"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("password_change/", views.PasswordChange.as_view(), name="password_change"),
    path("password_change/done/", views.PasswordChangeDone.as_view(), name="password_change_done"),
]

