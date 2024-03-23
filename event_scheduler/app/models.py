from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class EventStatus(models.Model):
    status=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.status}"

class Event(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField(max_length=2024)
    start=models.DateTimeField()
    duration=models.DurationField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    status=models.ForeignKey(EventStatus,on_delete=models.CASCADE,null=True)

