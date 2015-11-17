from django.contrib.auth.models import User
from django.test import TestCase
from django.db.models.signals import post_save

from gmi.django.profile.models import Profile
import gmi.django.profile.signals as signals


class ProfileSignalTestCase(TestCase):

    def test_ensure_profile(self):
        john = User.objects.create_user(
            'john', 'john@example.com', 'apassword', first_name='John')
        self.assertEqual(john.profile.about, '')

    def test_ensure_profile_preserve_existent(self):
        john = User.objects.create_user(
            'john', 'john@example.com', 'apassword', first_name='John')
        john.profile.about='kogeyHuvyai'
        signals.ensure_profile(sender=john.__class__, instance=john)
        self.assertEqual(john.profile.about, 'kogeyHuvyai')

    def test_ensure_profile_handles_signal(self):
        john = User(
            username='john',
            email='john@example.com',
            password='apassword',
            first_name='John')
        with self.assertRaises(ValueError):
            # post_save must raise, since John was not saved, so save() on 
            # related Profile is prohibited to prevent data loss.
           post_save.send(sender=john.__class__, instance=john)

    def test_ensure_profile_saves_profile(self):
        john = User.objects.create_user(
            'john', 'john@example.com', 'apassword', first_name='John')
        self.assertIsNotNone(john.profile.pk)
