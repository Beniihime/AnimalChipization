from django.db.models import QuerySet
from rest_framework import status
from animals.exceptions import ValidException
# from users.models import User
from django.core.exceptions import ObjectDoesNotExist
# "[1-9]{1}[0-9]*$"
from users import models
from users.models import User


class IdConverter:
    regex = "[1-9]{1}[0-9]*$"

    def to_python(self, value):
        return int(value)

    def to_url(self, value):
        return str(value)










