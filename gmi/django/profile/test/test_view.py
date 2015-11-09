from django.core.urlresolvers import reverse
from django.test import TestCase


class ProfileViewTestCase(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('profile:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Profile')

    def test_nonexistent_profile_view(self):
        response = self.client.get(reverse('profile:profile', args=('foo',)))
        self.assertEqual(response.status_code, 404)
