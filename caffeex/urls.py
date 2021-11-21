"""caffeex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from client.api.views import ClientCreateView
from car.api.views import CarListedView,CarDetailView
router = routers.DefaultRouter()

urlpatterns = [
    path('',include(router.urls)),
    path('client',ClientCreateView.as_view()),
    path('cars',CarListedView.as_view()),
    path('car/<str:plate>',CarDetailView.as_view()),
    path('admin/', admin.site.urls),
    path('auth', obtain_auth_token)
]
