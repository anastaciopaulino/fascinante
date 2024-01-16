from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from services.models import Service


def validate_data_hora(value):
    try:
        # Verificar se a string está no formato correto
        dia, mes_hora_min = value.split('/')
        mes, hora_min = mes_hora_min.split()
        int(dia)
        int(mes)
        hora, minuto = hora_min.split(':')
        int(hora)
        int(minuto)
    except (ValueError, IndexError):
        raise ValidationError('Formato inválido. Use o formato: DIA/MES HORA:MIN')


def validate_horario(value):
    if value < 8 or value > 18:
        raise ValidationError('As horas devem estar entre 08:00 e 18:00')


class Scheduling(models.Model):
    author = models.CharField(max_length=200, blank=False)
    checkin = models.CharField(max_length=20)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)

    def __str__(self):
      return f'{self.author}'