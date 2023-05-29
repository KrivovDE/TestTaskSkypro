from django.shortcuts import redirect
from django.urls import path, include, reverse

from .v1 import urlpatterns as urlpatterns_v1

app_name = "api"
urlpatterns = [
    path("", lambda request: redirect(to=reverse("api:api-docs_v1"))),
    path("api/", include(urlpatterns_v1)),
]
