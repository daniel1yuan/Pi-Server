from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.index, name='index'),
  url(r'^(?i)About/$', views.about, name='about'),
  url(r'^(?i)Contact/$', views.contact, name='contact'),
  url(r'^(?i)Portfolio/$', views.portfolio, name='portfolio'),
  url(r'^resume/$', views.resume, name='resume'),
  url(r'^_get_all_projects/$', views._get_all_projects),
]
