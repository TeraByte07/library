from rest_framework import serializers
from user_app.models import customUser
from .validators import validate_password_complexity
from django.core.exceptions import ValidationError
from catalogue_app.api.serializers import BorrowedBooksSerializer

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = customUser
        fields = ['username','first_name', 'last_name', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True}
        }

    def validate(self, data):
        # Checking if passwords match
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match"}, code='password_mismatch')
        
        # Checking if the email already exists
        if customUser.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({"email": "A user with this email already exists"}, code='email_exists')

        # Validating the password using custom validators
        try:
            validate_password_complexity(data['password'])
        except ValidationError as e:
            raise serializers.ValidationError({'password': list(e.messages)}, code='invalid_password')
        
        return data

    def create(self, validated_data):
        validated_data.pop('password2', None)
        user = customUser.objects.create_user(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        return user

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = customUser
        fields = ["username", "email"]
        
class userBorrowedBookSerializer(serializers.ModelSerializer):
    borrowed_books = BorrowedBooksSerializer(many=True, read_only=True)
    class Meta:
        model = customUser
        fields = ["username", "email", 'borrowed_books']