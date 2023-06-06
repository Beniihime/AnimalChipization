from rest_framework import status
from rest_framework.exceptions import APIException
from django.utils.encoding import force_str


class ValidException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'not valid'


class ValidUniqueException(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'Exists'


class Destroy(APIException):
    status_code = status.HTTP_200_OK
    default_detail = 'delete'
