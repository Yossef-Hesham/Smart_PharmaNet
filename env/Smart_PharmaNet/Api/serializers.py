from rest_framework import serializers
from .models import MyUser

from rest_framework import serializers
from .models import MyUser

class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = MyUser
        fields = ['name', 'email', 'password', 'password2', 'tc']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError('Password does not match')

        return attrs

    def create(self, validated_data):
        return MyUser.objects.create_user(**validated_data)
         