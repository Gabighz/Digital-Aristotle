from django.test import TestCase
from django.urls import reverse
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys


class IndexViewTests(TestCase):
    def test_no_chat(self):
        response = self.client.get(reverse('chatbot:index'))
        self.assertEqual(response.status_code, 200)


class ConversationTests(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        options = webdriver.ChromeOptions()
        options.headless = True
        cls.selenium = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=options)
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_conversation(self):
        self.selenium.get('%s%s' % (self.live_server_url, '/chatbot/'))
        user_input = self.selenium.find_element_by_name('textarea')
        user_input.send_keys('Hello')
        user_input.send_keys(Keys.RETURN)

