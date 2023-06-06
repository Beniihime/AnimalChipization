from datetime import datetime
from django.db import models
from users.models import User


class LocationManager(models.Manager):
    def create_location(self, latitude, longitude):
        point = self.model(
            latitude=self.create(latitude),
            longitude=self.create(longitude)
        )
        point.save(using=self._db)

        return point


class Locations(models.Model):
    objects = LocationManager()

    latitude = models.FloatField()
    longitude = models.FloatField()


class AnimalTypesManager(models.Manager):
    def create_type(self, type):
        types = self.model(
            type=self.create(type)
        )
        types.save(using=self._db)

        return types


class AnimalTypes(models.Model):
    objects = AnimalTypesManager()

    type = models.CharField(max_length=60, unique=True)


class Animal(models.Model):
    animalTypes = models.ManyToManyField(AnimalTypes, related_name='animalTypes', blank=True)
    weight = models.FloatField(verbose_name='weight')
    length = models.FloatField(verbose_name='length')
    height = models.FloatField(verbose_name='height')
    GENDER_CHOICE = (
        ('MALE', 'MALE'),
        ('FEMALE', 'FEMALE'),
        ('OTHER', 'OTHER'),
    )
    gender = models.CharField(verbose_name='gender', choices=GENDER_CHOICE, max_length=50)
    lifeStatus = models.CharField(verbose_name='lifeStatus', max_length=50, default='ALIVE')
    chippingDateTime = models.DateTimeField(auto_now_add=True, editable=False)

    chipperId = models.ForeignKey(User, on_delete=models.PROTECT)
    chippingLocationId = models.ForeignKey(Locations, on_delete=models.CASCADE)
    visitedLocations = models.ManyToManyField(Locations, related_name='visitedLocations', blank=True)

    deathDateTime = models.DateTimeField(null=True, editable=False)

    def __init__(self, *args, **kwargs):
        super(Animal, self).__init__(*args, **kwargs)
        self.old_lifeStatus = self.lifeStatus

    def save(self, *args, **kwargs):
        if self.lifeStatus == 'DEAD':
            self.deathDateTime = datetime.now()
        super(Animal, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.pk)
