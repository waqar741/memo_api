from rest_framework import serializers
from .models import Memo
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class MemoSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Memo
        fields = ['id', 'user', 'title', 'content', 'photo', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']
    #create memo with logged in user
    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)