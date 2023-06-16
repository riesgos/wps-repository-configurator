from django.urls import path
from . import views

urlpatterns = [
    path("export/<int:pk>.json/", views.process_json, name="process-json"),
]
