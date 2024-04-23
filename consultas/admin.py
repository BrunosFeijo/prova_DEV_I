from django.contrib import admin
from .models.paciente import Paciente
from .models.atendimento import Atendimento

# Register your models here.
admin.site.register(Paciente)
admin.site.register(Atendimento)