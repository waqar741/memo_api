from rest_framework import serializers
from .models import Memo

class MemoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Memo
        fields = ["id", "owner", "title", "content", "photo", "created_at", "updated_at"]
