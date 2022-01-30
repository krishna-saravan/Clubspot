from rest_framework.serializers import ModelSerializer, EmailField, ValidationError
from .models import UserAccount
from django.contrib.auth.models import User

class UserAccount_serializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields = '__all__'

class UpdateUserAccount_serializer(ModelSerializer):
    class Meta:
        model = UserAccount
        fields= (
            'nickName',
            'registration_number',
        )
