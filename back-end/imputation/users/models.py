from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from datetime import timedelta

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    approval = models.CharField(max_length=20, default='pending')
    role = models.CharField(max_length=50, default='user')
    organization = models.CharField(max_length=100, default='none')

    def __str__(self):
        return self.user.username
    
class OngoingProject(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    project_id = models.CharField(max_length=100)
    last_accessed = models.DateTimeField(auto_now=True)
    expiration_date = models.DateTimeField(default=timezone.now() + timedelta(weeks=1))
    resubmit = models.BooleanField(default=False)