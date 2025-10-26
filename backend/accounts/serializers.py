from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'  # use email instead of username

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        # Authenticate using email
        user = authenticate(username=email, password=password)
        if not user:
            raise AuthenticationFailed('Invalid credentials')

        data = super().validate({'username': email, 'password': password})
        return data
