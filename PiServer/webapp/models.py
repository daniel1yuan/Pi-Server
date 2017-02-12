from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Project(models.Model):
  project_name = models.CharField(max_length=30)
  date = models.DateField()
  project_link = models.TextField()
  project_description = models.TextField()
