from rest_framework import serializers
from .models import User,  Community

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        

class ComunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        fields = '__all__'