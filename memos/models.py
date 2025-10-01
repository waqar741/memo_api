from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Memo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="memos")
    title = models.CharField(max_length=2000)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.owner.username})"

