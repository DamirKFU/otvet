from http import HTTPStatus

from django.test import Client, TestCase


class HomePageEndPointTest(TestCase):
    def test_homepage_main_endpoint(self):
        respone = Client().get("")
        status_code = respone.status_code
        self.assertEqual(status_code, HTTPStatus.OK)
