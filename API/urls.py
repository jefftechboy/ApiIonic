"""
URL configuration for registrapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import re_path as url
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'api/seguridad/', SeguridadCodigosViewSet.as_view()),  # Para listar y crear usuarios
    
]
urlpatterns = format_suffix_patterns(urlpatterns)