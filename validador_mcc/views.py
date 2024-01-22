from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required


def index_page(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


@login_required
def edit_mccs(request: HttpRequest) -> HttpResponse:
    return render(request, "edit_mccs.html")
