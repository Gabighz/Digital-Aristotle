from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
import os


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
        self.assertContains(response, '<a class="btn btn-light action-button" role="button" href="%s">Logout</a>'
                            % reverse("logout"), html=True)

    def test_access_page_upload(self):
        # If the user is authenticated, they should be able to access the upload page of the admin area
        self.client.login(username="admin", password="password")

        response = self.client.get(reverse('admin_area:upload'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<a class="btn btn-light action-button" role="button" href="%s">Logout</a>'
                            % reverse("logout"), html=True)

    def test_file_upload_and_conversion(self):
        # Test whether lecture notes are successfully uploaded and stored on the system
        self.client.login(username="admin", password="password")
        test_file_path = "information_retrieval_system/test_input/ComputingComponents.pdf"

        with open(test_file_path, 'rb') as file:
            self.client.post(reverse('admin_area:upload'), {'file': file})

        uploaded_file_path = "information_retrieval_system/uploaded_files/ComputingComponents.pdf"
        converted_file_path = "information_retrieval_system/xml_files/ComputingComponents.xml"

        assert os.path.isfile(uploaded_file_path)
        assert os.path.isfile(converted_file_path)
