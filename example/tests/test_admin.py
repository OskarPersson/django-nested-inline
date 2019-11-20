from django.contrib.admin.sites import AdminSite
from django.test import SimpleTestCase

from example.app.admin import TopLevelAdmin
from example.app.models import TopLevel


class TopLevelAdminTestCasey(SimpleTestCase):
    def test_top_level(self):
        TopLevelAdmin(TopLevel, AdminSite())
