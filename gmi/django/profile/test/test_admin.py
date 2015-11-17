from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from django.test import TestCase

from gmi.django.profile.admin import ProfileAdmin
from gmi.django.profile.models import Profile


class MockRequest(object):
    pass


class MockSuperUser(object):
    def has_perm(self, perm):
        return True


request = MockRequest()
request.user = MockSuperUser()


class ProfileAdminTestCase(TestCase):

    def setUp(self):
        self.site = AdminSite()
        self.pa = ProfileAdmin(Profile, self.site)
        self.paul = User.objects.create_user(
            'paul', 'paul@example.com', 'apassword', first_name='Paul')
        self.john = User.objects.create_user(
            'john', 'john@example.com', 'apassword', first_name='John')
        self.john.profile.about = 'about'

    def test_profile_fields(self):
        self.assertEqual(list(self.pa.get_fields(request)), ['about'])

    def test_profile_list_display(self):
        # XXX test for exact name
        self.assertEqual(list(self.pa.get_list_display(request)), ['name'])

    def test_profile_change_forbidden(self):
        request.user = self.paul
        self.assertFalse(
            self.pa.has_change_permission(request, self.john.profile))

    def test_profile_change_allowed_for_own_profile(self):
        request.user = self.john
        self.assertTrue(
            self.pa.has_change_permission(request, self.john.profile))

    def test_profile_get_queryset(self):
        request.user = self.john
        self.assertEqual(
            list(self.pa.get_queryset(request)), [self.john.profile])
