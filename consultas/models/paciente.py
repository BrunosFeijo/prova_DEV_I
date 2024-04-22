from django.core.validators import MinLengthValidator

from consultas.models import *


class Paciente(BaseModels):
    nome = models.CharField(max_length=100, validators=[MinLengthValidator(10)])

    def __str__(self):
        return self.nome
