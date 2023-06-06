from rest_framework import generics
from rest_framework.permissions import *
from users.models import User
from users.serializers import RegisterSerializer, UserDetailSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from animals.permissions import AuthDontPermission, IsUserOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from users.service import PaginationClass, UserFilter


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AuthDontPermission]


class UserDetailApiView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsUserOwnerOrReadOnly)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_200_OK)

    def perform_destroy(self, instance):
        instance.delete()


class UserApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    pagination_class = PaginationClass
    filterset_class = UserFilter
