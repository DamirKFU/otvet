from django.urls import path, re_path, register_converter

import catalog.converters
import catalog.views

register_converter(catalog.converters.PositiveIntegerConverter, "pint")


urlpatterns = [
    path("", catalog.views.item_list),
    path("<int:pk>/", catalog.views.item_detail),
    re_path(r"re/(?P<pk>)[1-9][0-9]*/", catalog.views.item_detail),
    path("converter/<pint:pk>/", catalog.views.item_detail),
]
