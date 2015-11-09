from django.contrib.auth.models import User
from django.test import TestCase
from gmi.django.profile.models import Profile


class ProfileTestCase(TestCase):
    def setUp(self):
        self.john = User.objects.create_user(
            'john', 'john@example.com', 'apassword')
        self.john.save()
        profile = Profile.objects.create(about='foobar', user=self.john)

    def test_profile_extends_user(self):
        self.assertIsInstance(self.john.profile, Profile)

    def test_avatar_url(self):
        self.assertEqual(
            self.john.profile.avatar_url,
            'avatar/160x160/855f96e983f1f8e8be944692b6f719fd54329826cb62e98015efee8e2e071dd4.jpg')
