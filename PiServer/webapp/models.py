from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Project(models.Model):
  project_name = models.CharField(max_length=30, null=True)
  date = models.DateField(null=True)
  strDate = models.CharField(max_length=30, null=True)
  project_link = models.TextField(null=True)
  project_description = models.TextField(null=True)
  project_url = models.URLField(null=True)
  priority = models.IntegerField(default=0)
