from django.db import models
from django.contrib.auth.models import User

class Memo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} by {self.user.username}'