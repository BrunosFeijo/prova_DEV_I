from django.core.validators import MinLengthValidator

from consultas.models import *
from consultas.models.tipo_alergia import TipoAlergia


class Paciente(BaseModels):
    nome = models.CharField(max_length=100, validators=[MinLengthValidator(10)])
    cpf = models.CharField(max_length=11, validators=[MinLengthValidator(11)],
                           primary_key=True)  # não sei deixar unique, assim resolve
    endereco = models.CharField(max_length=100, validators=[MinLengthValidator(20)])
    cidade = models.CharField(max_length=50, validators=[MinLengthValidator(3)])
    tipo_alergia = models.CharField(max_length=100, choices=TipoAlergia)
    alergias = models.CharField(max_length=100, validators=[MinLengthValidator(5)], null=True)  # testar campo opcional
    telefone = models.CharField(max_length=20, validators=[MinLengthValidator(10)])
    telefone_emergencia = models.CharField(max_length=20, validators=[MinLengthValidator(10)])
    nome_contato = models.CharField(max_length=100, validators=[MinLengthValidator(10)])
    parentesco = models.CharField(max_length=20, validators=[MinLengthValidator(3)])

    def __str__(self):
        return self.nome
