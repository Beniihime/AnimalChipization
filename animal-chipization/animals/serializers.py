from rest_framework import serializers
from animals.models import Animal, AnimalTypes, Locations
from animals.exceptions import ValidUniqueException
from animals.custom_validators import valid_latitude, valid_longitude, valid_type


class AnimalTypesCreateSerializer(serializers.ModelSerializer):
    type = serializers.CharField(
        max_length=60,
        required=True,
        validators=[
            valid_type
        ]
    )

    class Meta:
        model = AnimalTypes
        fields = ['id', 'type']
        extra_kwargs = {
            'id': {'required': True}
        }

    def validate(self, data):
        _type = data.get('type')

        if AnimalTypes.objects.filter(type=_type).first():
            raise ValidUniqueException()
        return super().validate(data)

    def create(self, validated_data):
        types = AnimalTypes.objects.create(
            type=validated_data['type']
        )
        types.save()
        return types


class AnimalTypesDetailSerializer(serializers.ModelSerializer):

    type = serializers.CharField(
        max_length=60,
        required=True,
        validators=[
            valid_type
        ]
    )

    class Meta:
        model = AnimalTypes
        fields = ['id', 'type']

    def update(self, instance, validated_data):
        instance.type = validated_data.get('type', instance.type)

        instance.save()
        return instance

    def validate(self, data):
        _type = data.get('type')

        if AnimalTypes.objects.filter(type=_type).first():
            raise ValidUniqueException()
        return super().validate(data)


class AnimalDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Animal
        fields = ['id',
                  'animalTypes',
                  'weight',
                  'length',
                  'height',
                  'gender',
                  'lifeStatus',
                  'chippingDateTime',
                  'chipperId',
                  'chippingLocationId',
                  'visitedLocations',
                  'deathDateTime'
                  ]


class AnimalCreateSerializer(serializers.ModelSerializer):

    lifeStatus = serializers.ReadOnlyField()

    class Meta:
        model = Animal
        fields = ['id',
                  'animalTypes',
                  'weight',
                  'length',
                  'height',
                  'gender',
                  'lifeStatus',
                  'chippingDateTime',
                  'chipperId',
                  'chippingLocationId',
                  'visitedLocations',
                  ]


class LocationsCreateSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField(
        required=True,
        validators=[
            valid_latitude
        ]
    )
    longitude = serializers.FloatField(
        required=True,
        validators=[
            valid_longitude
        ]
    )

    class Meta:
        model = Locations
        fields = ['id', 'latitude', 'longitude']

    def validate(self, data):
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if Locations.objects.filter(latitude=latitude, longitude=longitude).first():
            raise ValidUniqueException()
        return super().validate(data)

    def create(self, validated_data):
        point = Locations.objects.create(
            latitude=validated_data['latitude'],
            longitude=validated_data['longitude']
        )
        point.save()
        return point


class LocationsSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField(
        required=True,
        validators=[
            valid_latitude
        ]
    )
    longitude = serializers.FloatField(
        required=True,
        validators=[
            valid_longitude
        ]
    )

    def create(self, validated_data):
        return Locations.objects.create(**validated_data)

    class Meta:
        model = Locations
        fields = '__all__'
