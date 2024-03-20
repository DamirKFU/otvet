from django.core.exceptions import ValidationError
import django.db


def perfect_validator(value):
    if "превосходно" in value.lower().split():
        return
    if "роскошно" in value.lower().split():
        return
    raise ValidationError("нету слова роскошно или превосходно")


class Item(django.db.models.Model):
    is_published = django.db.models.BooleanField(
        "опубликовано",
        default=True,
    )
    name = django.db.models.CharField(
        "название",
        max_length=150,
    )
    text = django.db.models.TextField("текст", validators=[perfect_validator])
