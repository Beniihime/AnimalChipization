"""restf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include, register_converter

from users.views import RegisterUserView

from restf.converters import IdConverter

# register_converter(IdConverter, "animal")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('animals.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('registration', RegisterUserView.as_view()),
    path('', include('users.urls')),
]
