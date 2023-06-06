from django.urls import path, register_converter
from users.views import *
from restf.converters import IdConverter

register_converter(IdConverter, "user")
app_name = 'users'
urlpatterns = [

    path('accounts/<user:pk>', UserDetailApiView.as_view()),
    path('accounts/search', UserApiView.as_view()),

]
