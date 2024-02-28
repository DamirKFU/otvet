from django.http import HttpResponse
from http import HTTPStatus


def homepage(request):
    return HttpResponse("Я чайник", status=HTTPStatus.IM_A_TEAPOT)
