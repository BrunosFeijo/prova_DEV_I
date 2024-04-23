# from django.contrib.auth import get_user_model
# User = get_user_model()
# User.objects.create_superuser('IFRS', 'qualquer@gmail.com', 'IFRS')
import time
from datetime import datetime

from consultas.models import Paciente, TipoAlergia, Parentesco, Atendimento, Plano, Prioridade

# paciente = Paciente.paciente_por_cpf("02406690024")
# print(paciente)
# pacientes = Paciente.objects.filter(atendimento__in__data="2024-04-22")
# print(pacientes)

i = 1
for i in range(1,4):
    paciente = Paciente.objects.create(
    nome = "Bruno Feijo" + str(i),
    cpf = '1234567890' + str(i),
    endereco = 'Rua Teste do Teste',
    cidade = 'Porto Alegre',
    tipo_paciente = TipoAlergia.DRUG,
    alergias = 'Qualquer alergia '+ str(i),
    telefone ='51985526703',
    telefone_emergencia = '51985526703',
    nome_contato = 'Thais Maciel Lima' + str(i),
    parentesco=Parentesco.PARTNER
    )
    paciente.save()

    atendimento = Atendimento.objects.create(
        data=datetime.now(),
        hora=time.time(),
        motivo='Atendimento',
        reconsulta=True,
        exames='Varios exames',
        encaminhamento='Qualquer encaminhamento',
        plano=Plano.PUBLIC,
        prioridade=Prioridade.LOW,
        paciente=Paciente.objects.get('1234567890' + str(i))
    )
    atendimento.save()
