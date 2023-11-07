from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    diseaseName = models.CharField(max_length=500, unique=True)
    buildversion = models.CharField(max_length=500)
    inputtype = models.CharField(max_length=500)
    input = models.CharField(max_length=500, blank=True, null=True)
    ref_raw = models.CharField(max_length=500)
    mafvalue = models.FloatField(max_length=500, blank=True, null=True)
    genovalue = models.FloatField(max_length=500, blank=True, null=True)
    hewvalue = models.FloatField(max_length=500, blank=True, null=True)
    infoscore = models.FloatField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=500, default="Queueing")
    progress = models.CharField(max_length=500, default="0%")





