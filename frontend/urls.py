from django.urls import path
from . import views


urlpatterns = [
    path(r'front', views.index ),
]