from django.conf.urls import include, url

urlpatterns = [
    url(r'^profile/', include('gmi.django.profile.urls', namespace='profile')),
]
