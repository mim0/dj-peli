from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pelis$', views.pelis, name='pelis'),
    url(r'^actores$', views.actores, name='actores')
]
