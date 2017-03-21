from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^(?i)About/$', views.about, name='about'),
  url(r'^resume/$', views.resume, name='resume'),
  url(r'^_get_all_projects/$', views._get_all_projects),
]
