from django.contrib.auth import get_user_model,authenticate
from django.db import models
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    '''serializer for the user object'''
    class Meta:
        model = get_user_model()
        # fields to include in the serializer
        fields = ('email', 'password','name')
        # extra settings in the model serializers
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        '''create a new user with encrypted password and 8 characters'''
        return get_user_model().objects.create_user(**validated_data)
        