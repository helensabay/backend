from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import AppUser, Profile  # <-- make sure these exist in accounts/models.py


# JWT serializer
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom JWT serializer; extend if you want extra claims."""
    pass


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
