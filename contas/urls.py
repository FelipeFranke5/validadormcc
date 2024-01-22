from django.urls import path
from . import views


app_name = "contas"
urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", views.CustomLogoutView.as_view(), name="logout"),
    path("registrar/", views.RegisterNewUser.as_view(), name="registrar"),
]
