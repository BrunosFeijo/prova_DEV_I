from django.utils.translation import gettext_lazy as _
from django.db import models


class Parentesco(models.TextChoices):
    FATHER = "Father", _("Pai")
    MOTHER = "Mother", _("Mãe")
    PARTNER = "Partner", _("Conjugê")
    OTHER = "Other", _("Outro")