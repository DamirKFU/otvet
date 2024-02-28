from django.test import TestCase, Client


class HomePageEndPointTest(TestCase):
    def test_homepage_main_endpoint(self):
        respone = Client().get("")
        status_code = respone.status_code
        self.assertEqual(status_code, 201)

    def test_content_main_homepage(self):
        respone = Client().get("")
        content = respone.content.decode()
        self.assertEqual(content, "Домашняя страница")
