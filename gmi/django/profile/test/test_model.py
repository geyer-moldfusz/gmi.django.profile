from django.test import TestCase

from gmi.django.profile.models import Profile
import gmi.django.profile.test as test


class ProfileTestCase(TestCase):
    def setUp(self):
        self.john = test.create_user()
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
