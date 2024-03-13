import re

from django.conf import settings


class ReverseRussianWordsMiddleware:
    count = 0

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        flag = ReverseRussianWordsMiddleware.count == 9
        if flag and settings.ALLOW_REVERSE:
            content = response.content.decode()
            words = re.findall(r"\b[а-я]+\b", content, re.IGNORECASE)
            for word in words:
                content = content.replace(word, word[::-1], 1)
            response.content = content.encode()
            ReverseRussianWordsMiddleware.count = 0
            return response
        ReverseRussianWordsMiddleware.count += 1
        return response
