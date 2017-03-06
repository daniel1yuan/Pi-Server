from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper
from django.core import serializers

from webapp.models import Project

import os
import json

def index(request):
  context = {
    'title': 'Daniel Yuan'
  }
  return render(request, 'webapp/index.html', context)

def resume(request):
  resumePath = os.path.join(os.getcwd(), "webapp", "static", "webapp", "files", "ResumeUIUC2016.pdf")
  response = HttpResponse(FileWrapper(file(resumePath,'rb')), content_type='application/pdf')
  response['Content-Disposition'] = 'attachment; filename="DanielYuanResume2016.pdf"'
  return response

# Routes for Database queries

def _get_all_projects(request):
  response = {};
  for project in Project.objects.all():
    priority = project.priority
    project = (serializers.serialize('json', [project]))
    if priority in response:
      response[priority].append(project)
    else:
      response[priority] = [project]
  return HttpResponse(json.dumps(response))
