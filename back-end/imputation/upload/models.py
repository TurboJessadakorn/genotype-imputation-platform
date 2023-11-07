from django.db import models
from django.utils.timezone import now
from projects.models import Project

# Create your models here.
class FileUpload(models.Model):
    file_id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=255)
    path = models.TextField(max_length=500)
    size = models.CharField(max_length=255)
    datetime_latest = models.DateTimeField(default=now, editable=False, blank=True)
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)