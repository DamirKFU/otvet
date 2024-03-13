from http import HTTPStatus

from django.test import Client, TestCase


class HomePageEndPointTest(TestCase):
    def test_about_main_endpoint(self):
        respone = Client().get("/about/")
        status_code = respone.status_code
        self.assertEqual(status_code, HTTPStatus.OK)
