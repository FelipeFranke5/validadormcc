from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("validador_mcc.urls")),
    path("contas/", include("contas.urls")),
]
