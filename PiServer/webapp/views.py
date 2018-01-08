from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing(request):
    context = {
        'title': 'Daniel Yuan'
    }
    return render(request, 'webapp/landing.html', context)
