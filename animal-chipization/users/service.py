import django_filters
from rest_framework import pagination
from rest_framework.response import Response
from .models import User
from animals.exceptions import ValidException


class PaginationClass(pagination.LimitOffsetPagination):
    max_limit = 50
    min_limit = 1
    min_offset = 0
    max_offset = 50
    limit_query_param = 'size'
    offset_query_param = 'from'

    def paginate_queryset(self, queryset, request, view=None):
        limit = request.query_params.get('size')
        offset = request.query_params.get('from')

        if limit:
            limit = int(limit)
            if limit > self.max_limit or limit < self.min_limit:
                raise ValidException
        if offset:
            offset = int(offset)
            if offset > self.max_offset or offset < self.min_offset:
                raise ValidException
        return super(self.__class__, self).paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        return Response(data)


class UserFilter(django_filters.FilterSet):
    firstName = django_filters.CharFilter(lookup_expr='icontains')
    lastName = django_filters.CharFilter(lookup_expr='icontains')
    email = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = User
        fields = ['firstName', 'lastName', 'email']





