from django.utils.translation import gettext_lazy as _
from django.db import models


class plano(models.TextChoices):
    UNIMED = "Unimed", _("Unimed")

