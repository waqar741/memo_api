from rest_framework import serializers
from .models import Memo
from django.contrib.auth.models import User

class MemoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Memo
        fields = ['id','user','title','photo','note','created_at','updated_at']
        read_only_fields = ('user',)
