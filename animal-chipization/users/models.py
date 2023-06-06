from django.db import models
from django.http import HttpResponse
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class MyUserManager(BaseUserManager):
    def _create_user(self, id, email, password, firstName, lastName, **extra_fields):
        if not email or password or firstName or lastName or id:
            return HttpResponse(status=400)
        user = self.model(
            email=self.normalize_email(email),
            **extra_fields,

        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, id, email, password, firstName, lastName):
        return self._create_user(id, email, password, firstName, lastName)

    def create_superuser(self, id, email, password, firstName, lastName):
        return self._create_user(id, email, password, firstName, lastName, is_staff=True, is_superuser=True)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstName', 'lastName']

    objects = MyUserManager()

    def __str__(self):
        return self.email

