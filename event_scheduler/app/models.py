from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Event(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField(max_length=2024)
    start=models.DateTimeField(name='Start At')
    duration=models.DurationField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)

