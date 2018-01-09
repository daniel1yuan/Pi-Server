from django.shortcuts import render
from django.http import HttpResponse
from wsgiref.util import FileWrapper

import os

# Create your views here.
def landing(request):
    context = {
        'title': 'Daniel Yuan'
    }
    return render(request, 'webapp/landing.html', context)

def about(request):
    context = {
        'title': 'Daniel Yuan: About'
    }
    return render(request, 'webapp/about.html', context)

def resume(request):
    PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    resumePath = os.path.join(PROJECT_ROOT, "static", "webapp", "files", "danielyuan_resume.pdf")
    response = HttpResponse(FileWrapper(open(resumePath,'rb')), content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="danielyuan_resume.pdf"'
    return response

def contact(request):
  context = {
    'title': 'Daniel Yuan'
  }
  return render(request, 'webapp/contact.html', context)
