from http import HTTPStatus

from django.test import Client, TestCase


class HomePageEndPointTest(TestCase):
    def test_homepage_main_endpoint(self):
        respone = Client().get("")
        status_code = respone.status_code
        self.assertEqual(status_code, HTTPStatus.OK)

    def test_homepage_coffee_endpoint(self):
        respone = Client().get("/coffee/")
        status_code = respone.status_code
        self.assertEqual(status_code, HTTPStatus.IM_A_TEAPOT)

    def test_homepage_coffee_content(self):
        respone = Client().get("/coffee/")
        content = respone.content.decode()
        self.assertEqual(content, "Я чайник")
