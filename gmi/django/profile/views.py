from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from contact_form.views import ContactFormView

from .models import Profile


class ProfileListView(ListView):

    model = Profile

    def get_context_data(self, **kwargs):
        context = super(ProfileListView, self).get_context_data(**kwargs)
        return context


class ProfileView(DetailView):

    model = User
    slug_field = 'username'
    template_name = 'profile/profile_detail.html'

    def __init__(self, **kwargs):
        super(ProfileView, self).__init__(**kwargs)
        self.contact_form_view = ContactFormView(**kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context.update(self.contact_form_view.get_context_data(**kwargs))
        context['profile'] = context['user'].profile
        return context
