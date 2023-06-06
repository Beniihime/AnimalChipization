from rest_framework import status
from rest_framework.exceptions import APIException


class UniqueEmailException(APIException):
    status_code = status.HTTP_409_CONFLICT
    default_detail = 'Email exists'


class ValidateIdException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = 'not valid id'

