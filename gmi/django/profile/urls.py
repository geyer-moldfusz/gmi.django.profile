from django.conf.urls import include, url

from .views import ProfileView, ProfileListView

urlpatterns = [
    url(r'^$', ProfileListView.as_view(), name='index'),
    url(r'^(?P<slug>[-\w]+)/$', ProfileView.as_view(), name='profile'),
]
