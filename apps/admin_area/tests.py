from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class IndexViewTests(TestCase):
    def setUp(self):
        # Sets up the necessary objects for testing authentication and permissions
        self.user = User.objects.create_superuser("admin", "admin@admin.com", "password")
        self.client = Client()

    def test_security_no_login(self):
        # If the user is not authenticated, they should receive a 302 (redirect) status
        response = self.client.get(reverse('admin_area:index'))
        self.assertEqual(response.status_code, 302)

    def test_access_page(self):
        # If the user is authenticated, they should be able to access the index of the admin area
        self.client.login(username="admin", password="password")

        response = self.client.get(reverse('admin_area:index'))
        self.assertEqual(response.status_code, 200)
