from django.urls import path
from . import views
from . import htmx_views


app_name = "validador_mcc"
urlpatterns = [
    path("", views.index_page, name="index"),
    path("editar_mccs/", views.edit_mccs, name="edit_mccs"),
]

# HTMX
htmx_urlpatterns = [
    path("create_new_mcc/", htmx_views.CreateNewMcc.as_view(), name="create_new_mcc"),
    path("list_mccs/", htmx_views.ListMccs.as_view(), name="list_mccs"),
    path("edit_mcc/<int:pk>/", htmx_views.EditMcc.as_view(), name="edit_mcc"),
    path("delete_mcc/<int:pk>/", htmx_views.DeleteMcc.as_view(), name="delete_mcc"),
    path(
        "validate_restricted_mcc/",
        htmx_views.ValidateRestrictedMcc.as_view(),
        name="validate_restricted_mcc",
    ),
]

urlpatterns += htmx_urlpatterns
