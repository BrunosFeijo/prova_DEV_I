from django.utils.translation import gettext_lazy as _
from django.db import models


class Prioridade(models.TextChoices):
    LOW = "1", _("Baixa")
    MEDIUM = "2", _("Média")
    HIGH = "3", _("Alta")
    URGENCY = "4", _("Urgência")
