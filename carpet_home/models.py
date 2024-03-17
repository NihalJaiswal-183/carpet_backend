import uuid
from django.db import models
from django.core.exceptions import ValidationError

from carpet_home.constants.enums import ColorEnum
from carpet_home.constants.exception_message import INVALID_CARPET_COLOR


def validate_carpet_color(value):
    if value not in ColorEnum.get_list_of_values():
        raise ValidationError(INVALID_CARPET_COLOR.format(value))


class Carpet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    carpet_color = models.CharField(max_length=50, validators=[validate_carpet_color])
