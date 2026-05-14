from rest_framework import serializers
from .models import User, Address


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('gsm_number', 'name', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            gsm_number=validated_data['gsm_number'],
            name=validated_data['name'],
            password=validated_data['password'],
            email=validated_data.get('email', '')
        )
        return user


class VerifyOTPSerializer(serializers.Serializer):
    gsm_number = serializers.CharField()
    otp_code   = serializers.CharField(max_length=6)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model  = User
        fields = ('id', 'gsm_number', 'name', 'email', 'is_buyer', 'is_seller', 'created_at')
        read_only_fields = ('id', 'created_at')


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Address
        fields = ('id', 'title', 'full_address', 'city', 'district', 'is_default')
        read_only_fields = ('id',)