from django.contrib import admin


import catalog.models


@admin.register(catalog.models.Item)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name",)
