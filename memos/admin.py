from django.contrib import admin
from .models import Memo

@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'created_at']
    list_filter = ['created_at', 'user']
    search_fields = ['title', 'content']