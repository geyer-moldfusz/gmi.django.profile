from django.core import mail
from django.core.urlresolvers import reverse
from django.test import TestCase

from gmi.django.profile.models import Profile
from gmi.django.profile.views import ProfileContactFormView
import gmi.django.profile.test as test


#class ProfileContactFormViewTestCase(TestCase):
#
#    def setUp(self):
#        self.john = test.create_user()
#        self.contact_form_view = ProfileContactFormView()
#        self.contact_form_view.kwargs = dict(slug='john')
#
#    def test_get(self):
#        self.contact_form_view.get(test.GetRequest)
#
#    def test_get_success_url(self):
#        self.assertEqual(self.contact_form_view.get_success_url(), '')


class ProfileTemplateTestCase(TestCase):
    def setUp(self):
        self.john = test.create_user(email='test@example.com')
        self.john.first_name = 'John'
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

    def test_contact(self):
        response = self.client.get(
            reverse('profile:contact_form', args=('john',)))
        self.assertContains(response, '<label for="id_name">')
        self.assertContains(response, '<label for="id_email">')
        self.assertContains(response, '<label for="id_body">')
        self.assertContains(response, '<input type="submit"')

    def test_contact_post(self):
        response = self.client.post(
            reverse('profile:contact_form', args=('john',)),
            dict(name='me', email='me@example.com', body='lorem ipsum'))
        self.assertRedirects(response, '/profile/john/contact/sent')
        self.assertEqual(mail.outbox[0].recipients(), ['test@example.com'])
        self.assertEqual(mail.outbox[0].subject, 'Contact form message')
