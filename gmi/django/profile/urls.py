from django.conf.urls import include, url
from django.views.generic import TemplateView

from .views import ProfileView, ProfileListView, ProfileContactFormView


urlpatterns = [
    url(r'^$', ProfileListView.as_view(), name='index'),
    url(r'^(?P<slug>[-\w]+)/$', ProfileView.as_view(), name='profile'),
    url(r'^(?P<slug>[-\w]+)/contact/$',
        ProfileContactFormView.as_view(),
        name='contact_form'),
    url(r'^(?P<slug>[-\w]+)/contact/sent$',
        TemplateView.as_view(
            template_name='contact_form/contact_form_sent.html'),
        name='contact_form_sent'),
]
