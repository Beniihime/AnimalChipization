import django_filters
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from users.models import User
from .models import Animal


class PaginationAnimals(LimitOffsetPagination):

    limit_query_param = 'size'
    offset_query_param = 'from'

    def get_paginated_response(self, data):
        return Response(data)


class AnimalFilter(django_filters.FilterSet):

    startDateTime = django_filters.IsoDateTimeFilter(lookup_expr='date__gt')
    endDateTime = django_filters.IsoDateTimeFilter(lookup_expr='date__lt')

    class Meta:
        model = Animal
        fields = ['startDateTime',
                  'endDateTime',
                  ]
