from django.contrib.auth.models import User, Permission
from django.core.urlresolvers import reverse
from django.test import TestCase

from gmi.django.profile.models import Profile


class ProfileTemplateTestCase(TestCase):
    def setUp(self):
        change_profile_permission = Permission.objects.get(
            codename='change_profile')
        self.john = User.objects.create_user(
            'john', 'john@example.com', 'apassword', first_name='John')
        self.john.is_staff=True
        self.john.user_permissions.add(change_profile_permission)
        self.john.save()

    def test_index(self):
        response = self.client.get(reverse('profile:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<ul id="profiles">')

    def test_index_context(self):
        response = self.client.get(reverse('profile:index'))
        self.assertQuerysetEqual(
            response.context_data['profile_list'],
            ['<Profile: Profile object>'],
            ordered=False)

    def test_index_avatar(self):
        response = self.client.get(reverse('profile:index'))
        self.assertContains(
            response,
            '<img src=/static/avatar/160x160/default.png class="avatar" />')

    def test_index_profile(self):
        response = self.client.get(reverse('profile:index'))
        self.assertContains(response, 'John')

    def test_index_profile_link(self):
        response = self.client.get(reverse('profile:index'))
        self.assertContains(response, '<a href="/profile/john/"')

    def test_profile_nonexistent(self):
        response = self.client.get(reverse('profile:profile', args=('foo',)))
        self.assertEqual(response.status_code, 404)

    def test_profile(self):
        response = self.client.get(reverse('profile:profile', args=('john',)))
        self.assertEqual(response.status_code, 200)

    def test_profile_name(self):
        response = self.client.get(reverse('profile:profile', args=('john',)))
        self.assertContains(response, '<h1 id="name">John</h1>')

    def test_profile_avatar(self):
        response = self.client.get(reverse('profile:profile', args=('john',)))
        self.assertContains(
            response,
            '<img src=/static/avatar/320x320/default.png class="avatar" />')

    def test_profile_about_markdown(self):
        self.john.profile.about='about_test_Eryupht\n==='
        self.john.profile.save()
        response = self.client.get(reverse('profile:profile', args=('john',)))
        self.assertContains(response, '<h1>about_test_Eryupht</h1>')

    def test_profile_about_markdown_html_safe(self):
        self.john.profile.about = "<html id='inline'>inline html</html>"
        self.john.profile.save()
        response = self.client.get(reverse('profile:profile', args=('john',)))
        self.assertNotContains(response, "<html id='inline'>")

    def test_profile_about_markdown_html_comment(self):
        self.john.profile.about = "<html id='inline'>inline html</html>"
        self.john.profile.save()
        response = self.client.get(reverse('profile:profile', args=('john',)))
        self.assertContains(response, '[HTML_REMOVED]')
