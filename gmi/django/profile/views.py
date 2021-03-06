from contact_form.views import ContactFormView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import Http404
from django.views.generic.detail import DetailView, SingleObjectMixin
from django.views.generic.list import ListView

from .models import Profile


class ProfileListView(ListView):
    model = Profile


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
        self._prepare_request()
        return super(ProfileContactFormView, self).get(
            request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self._prepare_request()
        return super(ProfileContactFormView, self).post(
            request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super(ProfileContactFormView, self).get_form_kwargs()
        kwargs.update(dict(recipient_list=[self.object.email]))
        return kwargs

    def get_success_url(self):
        return reverse(
            'profile:contact_form_sent', args=(self.object.username,))

    def _prepare_request(self):
        self.object = self.get_object()
        if not self.object.email:
            raise Http404("No contact options")
