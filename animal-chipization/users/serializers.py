from rest_framework import serializers
from users.models import User
from users.exceptions import UniqueEmailException, ValidateIdException


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
    )
    password = serializers.CharField(
        write_only=True, required=True)

    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName', 'email', 'password']
        extra_kwargs = {
            'id': {'required': True},
            'firstName': {'required': True},
            'lastName': {'required': True}
        }

    def validate_email(self, value):
        if value is not None:
            exist_email = User.objects.filter(email=value).first()
            if exist_email:
                raise UniqueEmailException()
            return value

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            firstName=validated_data['firstName'],
            lastName=validated_data['lastName'],
            # id=validated_data['id']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserDetailSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True
    )

    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName', 'email', 'password']
        extra_kwargs = {
            'id': {'required': True},
            'firstName': {'required': True},
            'lastName': {'required': True}
        }

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.firstName = validated_data.get('firstName', instance.firstName)
        instance.lastName = validated_data.get('lastName', instance.lastName)

        instance.set_password(validated_data.get('password'))
        instance.save()
        return instance


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=False
    )

    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName', 'email', 'password']
        extra_kwargs = {
            'id': {'required': True},
            'firstName': {'required': True},
            'lastName': {'required': True}
        }
