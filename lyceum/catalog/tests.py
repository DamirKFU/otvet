from http import HTTPStatus

from django.test import Client, TestCase
import parameterized


class HomePageEndPointTest(TestCase):
    def test_catalog_main_endpoint(self):
        respone = Client().get("/catalog/")
        status_code = respone.status_code
        self.assertEqual(status_code, HTTPStatus.OK)

    @parameterized.parameterized.expand(
        [
            ("0", HTTPStatus.OK),
            ("1", HTTPStatus.OK),
            ("100", HTTPStatus.OK),
            ("110", HTTPStatus.OK),
            ("abs", HTTPStatus.NOT_FOUND),
            ("1a", HTTPStatus.NOT_FOUND),
            ("a1", HTTPStatus.NOT_FOUND),
            ("%1", HTTPStatus.NOT_FOUND),
            ("1%", HTTPStatus.NOT_FOUND),
            ("0.121", HTTPStatus.NOT_FOUND),
            ("3.121", HTTPStatus.NOT_FOUND),
        ]
    )
    def test_catalog_item_detail_1_endpoint(self, param, expected_status):
        respone = Client().get(f"/catalog/{param}/")
        status_code = respone.status_code
        self.assertEqual(status_code, expected_status)
