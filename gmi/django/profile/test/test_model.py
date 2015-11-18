from django.contrib.auth.models import User, Permission
from django.test import TestCase

from gmi.django.profile.models import Profile


class ProfileTestCase(TestCase):
    def setUp(self):
        change_profile_permission = Permission.objects.get(
            codename='change_profile')
        self.john = User.objects.create_user(
            'john', 'john@example.com', 'apassword')
        self.john.is_staff=True
        self.john.user_permissions.add(change_profile_permission)
        self.john.save()
        self.john.profile.about = 'foobar'

    def test_profile_extends_user(self):
        self.assertIsInstance(self.john.profile, Profile)

    def test_about(self):
        self.assertEqual(self.john.profile.about, 'foobar')

    def test_name_only_username(self):
        self.assertEqual(self.john.profile.name, 'john')

    def test_name_first_name(self):
        self.john.first_name = 'John'
        self.assertEqual(self.john.profile.name, 'John')

    def test_name_first_and_last_name(self):
        self.john.first_name = 'John'
        self.john.last_name = 'Doe'
        self.assertEqual(self.john.profile.name, 'John Doe')

    def test_name_only_last_name(self):
        self.john.last_name = 'Doe'
        self.assertEqual(self.john.profile.name, 'john')
