from django import VERSION
from django.contrib.auth.models import User
from django.template.response import TemplateResponse
from django.test import TestCase
if VERSION < (2, 0, 0):
    from django.core.urlresolvers import reverse
else:
    from django.urls import reverse


class TopLevelAdminTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.superuser = User.objects.create_superuser(username='super', password='secret', email='super@example.com')

    def setUp(self):
        try:
            self.client.force_login(self.superuser)
        except AttributeError:
            self.client.login(username=self.superuser.username, password='secret')

    def test_changelist(self):
        response = self.client.get(reverse('admin:app_toplevel_changelist'))
        self.assertIsInstance(response, TemplateResponse)
        self.assertEqual(response.status_code, 200)

    def test_add_view(self):
        response = self.client.get(reverse('admin:app_toplevel_add'))
        self.assertIsInstance(response, TemplateResponse)
        self.assertEqual(response.status_code, 200)
