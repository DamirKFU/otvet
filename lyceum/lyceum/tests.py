from django.test import Client, override_settings, TestCase


class RussianWordsReverseTest(TestCase):
    @override_settings(ALLOW_REVERSE=True)
    def test_middleware_enable(self):
        contents = [
            Client().get("/coffee/").content.decode() for _ in range(10)
        ]
        self.assertIn("Я кинйач", contents)

    @override_settings(ALLOW_REVERSE=False)
    def test_middleware_off(self):
        contents = [
            Client().get("/coffee/").content.decode() for _ in range(10)
        ]
        self.assertNotIn("Я кинйач", contents)
