from rest_framework import serializers
from .models import AppUser
from api.models import Profile  # adjust if Profile is in accounts.models

class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=Profile.ROLE_CHOICES, required=True)

    class Meta:
        model = AppUser
        fields = ['first_name', 'last_name', 'email', 'password', 'role']

    def create(self, validated_data):
        role = validated_data.pop('role')
        password = validated_data.pop('password')
        first_name = validated_data.pop('first_name')
        last_name = validated_data.pop('last_name')

        # Create user
        user = AppUser.objects.create(**validated_data)
        user.set_password(password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()

        # Create profile
        Profile.objects.create(user=user, role=role)

        return user
