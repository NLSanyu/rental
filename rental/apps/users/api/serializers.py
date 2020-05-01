from rest_framework import serializers

from rental.apps.users.models import User


class RegistrationSerializer(serializers.ModelSerializer):
    # Passwords should be at least 8 characters long, up to 128 characters
    # and can not be read by the client
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'token']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
