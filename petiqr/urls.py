"""petiqr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url
from petiqrContainer import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'petiqr/countries', views.CountriesAPIView.as_view(), name='countries-list'),
    path(r'petiqr/states', views.StatesAPIView.as_view(), name='states-list'),
    path(r'petiqr/cities', views.CitiesAPIView.as_view(), name='cities-list'),
    path(r'petiqr/owners', views.OwnersAPIView.as_view(), name='owners-list'),    
    path('', include('frontend.urls')),
]