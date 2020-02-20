from unittest import skipIf

from django import VERSION
from django.contrib.auth.models import Permission, User
from django.template.response import TemplateResponse
from django.test import TestCase

from example.app.models import TopLevel

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse




class TopLevelAdminTestCase(TestCase):
    def setUp(self):
        self.superuser = User.objects.create_superuser(username='super', password='secret', email='super@example.com')
        self.user = User.objects.create_user(
            username='user', password='secret', email='user@example.com',
        )
        self.user.is_staff = True
        self.user.save()

    def login(self, user):
        try:
            self.client.force_login(user)
        except AttributeError:
            self.client.login(username=user.username, password='secret')

    def test_changelist(self):
        self.login(self.superuser)

        response = self.client.get(reverse('admin:app_toplevel_changelist'))
        self.assertIsInstance(response, TemplateResponse)
        self.assertEqual(response.status_code, 200)

    def test_add_view(self):
        self.login(self.superuser)

        response = self.client.get(reverse('admin:app_toplevel_add'))
        self.assertIsInstance(response, TemplateResponse)
        self.assertEqual(response.status_code, 200)

    def test_change_view(self):
        change_perm = Permission.objects.get(codename='change_toplevel')
        self.user.user_permissions.add(change_perm)
        self.login(self.user)

        obj = TopLevel.objects.create()
        response = self.client.get(reverse('admin:app_toplevel_change', args=(obj.pk,)))
        self.assertIsInstance(response, TemplateResponse)
        self.assertEqual(response.status_code, 200)

    @skipIf(VERSION < (2, 1), 'view permission was added in Django 2.1')
    def test_read_only_change_view(self):
        view_perm = Permission.objects.get(codename='view_toplevel')
        self.user.user_permissions.add(view_perm)
        self.login(self.user)

        obj = TopLevel.objects.create()
        response = self.client.get(reverse('admin:app_toplevel_change', args=(obj.pk,)))
        self.assertIsInstance(response, TemplateResponse)
        self.assertEqual(response.status_code, 200)
