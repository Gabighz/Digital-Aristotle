from django.test import TestCase
from django.urls import reverse


class IndexViewTests(TestCase):
    def test_access_page(self):
        response = self.client.get(reverse('admin_area:index'))
        self.assertEqual(response.status_code, 200)
