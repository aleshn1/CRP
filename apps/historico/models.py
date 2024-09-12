from django.db import models

from apps.members.models import Membros
from apps.pastorais.models import Pastorais
from crp import settings


class Historico(models.Model):
    membro = models.ForeignKey(Membros, on_delete=models.CASCADE)
    novo_elo = models.CharField(max_length=50)
    nova_pastoral = models.ForeignKey(Pastorais, on_delete=models.SET_NULL, null=True, blank=True)
    pastorais_atuais = models.ManyToManyField(Pastorais, related_name='historicos_atuais', blank=True)
    pastorais_adicionadas = models.ManyToManyField(Pastorais, related_name='historicos_adicionados', blank=True)
    pastorais_removidas = models.ManyToManyField(Pastorais, related_name='historicos_removidos', blank=True)
    data_mudanca = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f'Histórico de Mudanças para {self.membro.nome_completo}'
