from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<username>[A-Za-z0-9]+)/$', views.profile, name='profile'),
]
