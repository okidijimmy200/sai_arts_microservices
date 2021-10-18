from django.contrib.auth import get_user_model,authenticate
from django.utils.translation import ugettext_lazy as _
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

class AuthTokenSerializer(serializers.Serializer):
    '''serializer for the user authentication object'''
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )
    # validation command
    def validate(self, attrs):
        # validate and authenticate user
        email = attrs.get('email')
        password = attrs.get('password')

        # authenticate requests
        user = authenticate(
            # request to authenticate
            request = self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            msg = _('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        # set user in attrs
        attrs['user'] = user
        return attrs



        