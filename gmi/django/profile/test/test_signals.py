from django.test import TestCase
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from unittest.mock import Mock

from gmi.django.profile.models import Profile
import gmi.django.profile.signals as signals
import gmi.django.profile.test as test


class ProfileSignalTestCase(TestCase):

    def setUp(self):
        self.john = test.create_user()

    def test_ensure_profile(self):
        self.assertEqual(self.john.profile.about, '')

    def test_ensure_profile_no_profile_if_not_staff(self):
        george = User(username='george')
        george.has_perm = Mock()
        george.has_perm.return_value = True
        signals.ensure_profile(sender=george.__class__, instance=george)
        with self.assertRaises(Profile.DoesNotExist):
            george.profile

    def test_ensure_profile_no_profile_if_no_permission(self):
        george = User(username='george')
        george.is_staff = True
        george.has_perm = Mock()
        george.has_perm.return_value = False
        signals.ensure_profile(sender=george.__class__, instance=george)
        with self.assertRaises(Profile.DoesNotExist):
            george.profile

    def test_ensure_profile_preserve_existent(self):
        self.john.profile.about='kogeyHuvyai'
        signals.ensure_profile(sender=self.john.__class__, instance=self.john)
        self.assertEqual(self.john.profile.about, 'kogeyHuvyai')

    def test_ensure_profile_handles_signal(self):
        george = User(username='george', is_staff=True)
        george.has_perm = Mock()
        george.has_perm.return_value = True
        with self.assertRaises(ValueError):
            # post_save must raise, since John was not saved, so save() on 
            # related Profile is prohibited to prevent data loss.
           post_save.send(sender=george.__class__, instance=george)

    def test_ensure_profile_saves_profile(self):
        paul = test.create_user(username='paul')
        self.assertIsNotNone(paul.profile.pk)
