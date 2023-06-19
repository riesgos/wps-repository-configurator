from django.shortcuts import redirect
from django.urls import reverse


def index(request):
    url = reverse("admin:index")
    return redirect(url)
