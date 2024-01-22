from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import View
from .models import RestrictedMcc
from .forms import RestrictedMccModelForm


class CreateNewMcc(View):
    http_method_names = ["get", "post"]

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = RestrictedMccModelForm()
        return render(request, "htmx/create_new_mcc.html", {"form": form})

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        form = RestrictedMccModelForm(request.POST)

        if form.is_valid():
            form.save()
            new_empty_form = RestrictedMccModelForm()
            return render(
                request,
                "htmx/create_new_mcc.html",
                {"form": new_empty_form, "created": True},
            )
        return render(request, "htmx/create_new_mcc.html", {"form": form})


class ListMccs(View):
    http_method_names = ["get"]

    def get(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        mccs = RestrictedMcc.objects.all()
        return render(request, "htmx/list_mccs.html", {"mccs": mccs})


class EditMcc(View):
    http_method_names = ["get", "post"]

    def get(
        self, request: HttpRequest, pk: int, *args: str, **kwargs: Any
    ) -> HttpResponse:
        try:
            current_mcc = RestrictedMcc.objects.get(pk=pk)
        except RestrictedMcc.DoesNotExist:
            return render(request, "htmx/mcc_not_found.html")

        form = RestrictedMccModelForm(instance=current_mcc)
        return render(request, "htmx/edit_mcc.html", {"form": form, "mcc": current_mcc})

    def post(
        self, request: HttpRequest, pk: int, *args: str, **kwargs: Any
    ) -> HttpResponse:
        try:
            current_mcc = RestrictedMcc.objects.get(pk=pk)
        except RestrictedMcc.DoesNotExist:
            return render(request, "htmx/mcc_not_found.html")

        form = RestrictedMccModelForm(request.POST, instance=current_mcc)

        if form.is_valid():
            form.save()
            return render(
                request, "htmx/mcc_successfully_edited.html", {"mcc": current_mcc}
            )
        return render(request, "htmx/edit_mcc.html", {"form": form, "mcc": current_mcc})


class DeleteMcc(View):
    http_method_names = ["post"]

    def post(
        self, request: HttpRequest, pk: int, *args: str, **kwargs: Any
    ) -> HttpResponse:
        try:
            current_mcc = RestrictedMcc.objects.get(pk=pk)
        except RestrictedMcc.DoesNotExist:
            return render(request, "htmx/mcc_not_found.html")

        current_mcc.delete()
        return render(request, "htmx/mcc_successfully_deleted.html")


def render_typed_mcc_validation(
    request: HttpRequest, return_text: str, return_text_color: str
) -> HttpResponse:
    context = {"return_text": return_text, "return_text_color": return_text_color}
    return render(request, "htmx/typed_mcc_validation.html", context)


class ValidateRestrictedMcc(View):
    http_method_names = ["post"]

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        typed_mcc = request.POST.get("mcc")

        if typed_mcc is None:
            return_text = "Campo Vazio!"
            return_text_color = "text-danger fw-bold"
            return render_typed_mcc_validation(request, return_text, return_text_color)

        str_typed_mcc = str(typed_mcc)

        if len(str_typed_mcc) != 4:
            return_text = "O MCC deve conter 4 dígitos."
            return_text_color = "text-danger fw-bold"
            return render_typed_mcc_validation(request, return_text, return_text_color)

        try:
            matched_mcc = RestrictedMcc.objects.get(code=int(str_typed_mcc))
            return_text = f"MCC restrito para credenciamento. Nome: {matched_mcc.name}."
            return_text_color = "text-danger fw-bold"
        except RestrictedMcc.DoesNotExist:
            return_text = "MCC válido!"
            return_text_color = "text-success"
        return render_typed_mcc_validation(request, return_text, return_text_color)
