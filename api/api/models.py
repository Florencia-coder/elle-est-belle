from django.db import models

# Create your models here.
class Comments(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Album(models.Model):
    month = models.IntegerField()
    images = models.JSONField()