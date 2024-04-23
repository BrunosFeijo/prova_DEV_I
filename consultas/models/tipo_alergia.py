from django.utils.translation import gettext_lazy as _
from django.db import models


class TipoAlergia(models.TextChoices):
    FOOD = "FOOD", _("Comida")
    DRUG = "DRUG", _("Medicamentos")
    INSECT = "INSECT", _("Insetos")
    OTHER = "OTHER", _("Outros")