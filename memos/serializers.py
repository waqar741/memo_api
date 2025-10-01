from rest_framework import serializers
from .models import Memo
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MemoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Memo
        fields = ["id", "owner", "title", "content", "photo", "created_at", "updated_at"]


