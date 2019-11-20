from django.contrib.admin.sites import AdminSite
from django.test import SimpleTestCase

from example.app.admin import TopLevelAdmin
from example.app.models import TopLevel


class TestSubquery(SimpleTestCase):
    def test_with_count(self):
        TopLevelAdmin(TopLevel, AdminSite())
