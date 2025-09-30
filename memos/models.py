from django.db import models
from django.contrib.auth.models import User

class Memo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='memos')
    title = models.CharField(max_length=2000)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    note = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
