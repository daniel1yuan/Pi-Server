from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper
import os

def index(request):
  context = {
    'title': 'Daniel Yuan'
  }
  return render(request, 'webapp/index.html', context)

def about(request):
  context = {
    'title': 'Daniel Yuan'
  }
  return render(request, 'webapp/about.html', context)

def portfolio(request):
  context = {
    'title': 'Daniel Yuan'
  }
  return render(request, 'webapp/portfolio.html', context)

def contact(request):
  context = {
    'title': 'Daniel Yuan'
  }
  return render(request, 'webapp/contact.html', context)

def contact(request):
  context = {
    'title': 'Daniel Yuan'
  }
  return render(request, 'webapp/contact.html', context)

def resume(request):
  resumePath = os.path.join(os.getcwd(), "webapp", "static", "webapp", "files", "ResumeUIUC2016.pdf")
  response = HttpResponse(FileWrapper(file(resumePath,'rb')), content_type='application/pdf')
  response['Content-Disposition'] = 'attachment; filename="DanielYuanResume2016.pdf"'
  return response
