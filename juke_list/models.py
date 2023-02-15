from django.db import models

# Create your models here.

class Video(models.Model):
    tags = models.CharField(max_length=50)
    link = models.CharField(max_length=500)
    thumbnail = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)