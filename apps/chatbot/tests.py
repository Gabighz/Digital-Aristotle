from django.test import TestCase
from django.urls import reverse


class IndexViewTests(TestCase):
    def test_no_chat(self):
        response = self.client.get(reverse('chatbot:index'))
        self.assertEqual(response.status_code, 200)
