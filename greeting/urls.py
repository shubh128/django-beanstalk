from django.urls import path
from .views import greeting, jsongreeting

urlpatterns = [
    path('world', greeting),
    path('world/json', jsongreeting)
]
