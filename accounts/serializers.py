from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'password')

    def create(self, validated):
        user = User.objects.create_user(
            email=validated['email'],
            username=validated.get('username', validated['email'].split('@')[0]),
            password=validated['password'],
        )
        return user
