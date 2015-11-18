from contact_form.views import ContactFormView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.list import ListView

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

    def get_context_data(self, **kwargs):
        context = super(ProfileView, self).get_context_data(**kwargs)
        context['profile'] = context['user'].profile
        return context


class ProfileContactFormView(SingleObjectMixin, ContactFormView):
    model = User
    slug_field = 'username'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(ProfileContactFormView, self).get(
            request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super(ProfileContactFormView, self).post(
            request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(ProfileContactFormView, self).get_form_kwargs()
        kwargs.update(dict(recipient_list=[self.object.email]))
        return kwargs

    def get_success_url(self):
        context = self.get_context_data()
        return reverse(
            'profile:contact_form_sent', args=(context['user'].username,))
