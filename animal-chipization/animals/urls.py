from django.template.defaulttags import url
from django.urls import path, register_converter

from animals.views import *
from restf.converters import IdConverter

register_converter(IdConverter, "animal")


app_name = 'animal'
urlpatterns = [
    path('animals', AnimalCreateView.as_view()),
    path('animals/<animal:pk>', AnimalDetailApiView.as_view()),
    path('animals/types', AnimalTypesCreateView.as_view()),
    path('animals/types/<animal:pk>', AnimalTypesApiView.as_view()),
    path('locations', LocationCreateView.as_view()),
    path('locations/<animal:pk>', LocationApiView.as_view()),
    path('animals/search', AnimalView.as_view())
]
