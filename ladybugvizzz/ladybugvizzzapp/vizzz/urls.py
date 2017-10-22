# vizzz/urls.py
from django.conf.urls import url
from vizzz import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
