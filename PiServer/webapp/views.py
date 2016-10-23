from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  context = {
    'title': 'Daniel Yuan'
  }

  return render(request, 'webapp/index.html', context)

def about(request):
  return render(request, 'about.html', {})
