from django.forms import ModelForm
from django.test import TestCase

from gmi.django.profile.models import Profile


class ProfileFormTestCase(TestCase):

    class ProfileForm(ModelForm):
        class Meta:
            model = Profile
            fields = ['about']

    def test_about_empty(self):
        form = self.ProfileForm(dict(about=None))
        self.assertTrue(form.is_valid())

