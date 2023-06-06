from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status
from animals.serializers import *
from animals.models import Animal
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from animals.service import AnimalFilter
from users.service import PaginationClass


class AnimalCreateView(generics.CreateAPIView):

    queryset = Animal.objects.all()
    serializer_class = AnimalCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AnimalDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Animal.objects.all()
    serializer_class = AnimalDetailSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()


class AnimalTypesCreateView(generics.CreateAPIView):
    serializer_class = AnimalTypesCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = AnimalTypes.objects.all()


class AnimalTypesApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AnimalTypesDetailSerializer
    queryset = AnimalTypes.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()


class AnimalView(generics.ListAPIView):

    queryset = Animal.objects.all()
    serializer_class = AnimalDetailSerializer
    filter_backends = [DjangoFilterBackend]
    pagination_class = PaginationClass
    filterset_class = AnimalFilter


class LocationCreateView(generics.CreateAPIView):
    serializer_class = LocationsCreateSerializer
    queryset = Locations.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]


class LocationApiView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = LocationsSerializer
    queryset = Locations.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()

