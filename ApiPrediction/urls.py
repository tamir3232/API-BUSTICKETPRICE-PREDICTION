# myapp/urls.py
from django.urls import path
from .viewset_api import testingyaa

urlpatterns = [
    path('predict', testingyaa.as_view()),
]
