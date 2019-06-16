from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class AdminAreaViewTests(TestCase):
    def setUp(self):
        # Sets up the necessary objects for testing authentication and permissions
        self.user = User.objects.create_superuser("admin", "admin@admin.com", "password")
        self.client = Client()

    def test_security_no_login_index(self):
        # If the user is not authenticated, they should receive a 302 (redirect) status
        response = self.client.get(reverse('admin_area:index'))
        self.assertEqual(response.status_code, 302)

    def test_security_no_login_upload(self):
        # If the user is not authenticated, they should receive a 302 (redirect) status
        response = self.client.get(reverse('admin_area:upload'))
        self.assertEqual(response.status_code, 302)

    def test_access_page_index(self):
        # If the user is authenticated, they should be able to access the index of the admin area
        self.client.login(username="admin", password="password")

        response = self.client.get(reverse('admin_area:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="%s">Logout</a>' % reverse("logout"), html=True)

    def test_access_page_upload(self):
        # If the user is authenticated, they should be able to access the index of the admin area
        self.client.login(username="admin", password="password")

        response = self.client.get(reverse('admin_area:upload'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a href="%s">Logout</a>' % reverse("logout"), html=True)
