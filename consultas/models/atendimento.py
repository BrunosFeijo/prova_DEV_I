from django.core.validators import MinLengthValidator

from consultas.models import *
from . import Prioridade
from .plano import Plano
from .paciente import Paciente


class Atendimento(BaseModels):
    data = models.DateField()
    hora = models.TimeField()
    motivo = models.CharField(max_length=200,validators=[MinLengthValidator(10)])
    reconsulta = models.BooleanField(default=False)
    exames = models.CharField(max_length=200,validators=[MinLengthValidator(5)])
    encaminhamentos = models.CharField(max_length=500,validators=[MinLengthValidator(10)])
    plano = models.CharField(max_length=20, choices=Plano)
    prioridade = models.CharField(max_length=1, choices=Prioridade)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.data} - {self.hora} : {self.motivo} - {self.prioridade} - {self.plano}'

