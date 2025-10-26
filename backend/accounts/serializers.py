from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import AppUser, Profile  # <-- make sure these exist in accounts/models.py
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model, authenticate
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import get_user_model, authenticate
User = get_user_model()


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    email = serializers.EmailField(write_only=True)

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({'detail': 'Invalid credentials'})

        if not user.check_password(password):
            raise serializers.ValidationError({'detail': 'Invalid credentials'})

        # Map username for SimpleJWT
        attrs['username'] = user.username
        return super().validate(attrs)
# Registration serializer
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = AppUser
        fields = ["email", "password", "first_name", "last_name", "role"]

    def create(self, validated_data):
        user = AppUser.objects.create(
            email=validated_data["email"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            role=validated_data.get("role", "user"),
            status="active",
        )
        user.set_password(validated_data["password"])
        user.save()

        # Optional: create related Profile if your model has one
        Profile.objects.create(user=user, role=user.role)
        return user
