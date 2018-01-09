from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('About', views.about, name='about'),
    path('Resume', views.resume, name='resume'),
    path('Contact', views.contact, name='contact')
]
