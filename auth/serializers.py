from rest_captcha.serializers import RestCaptchaSerializer
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer


class AuthenticationSerializer(RestCaptchaSerializer, AuthTokenSerializer):
    username = serializers.CharField(max_length=64)
    password = serializers.CharField(max_length=64)

    def validate(self, data):
        captcha_serializer = RestCaptchaSerializer(data=data)
        captcha_serializer.is_valid(raise_exception=True)

        auth_serializer = AuthTokenSerializer(data=data)
        auth_serializer.is_valid(raise_exception=True)
        user = auth_serializer.validated_data['user']

        return user
