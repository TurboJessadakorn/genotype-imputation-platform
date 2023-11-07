from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class UserActivityLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=100)
    activity_time = models.DateTimeField(default=timezone.now)
    description = models.TextField(default='none')
