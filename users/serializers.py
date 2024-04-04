from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def validate_username(self, value):
        if len(value) < 4:
            raise serializers.ValidationError('Username length should be minimum 4 characters long.')
        return value

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        user.is_active = True
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email= serializers.EmailField(max_length=30)
    password = serializers.CharField(max_length=30)

        
