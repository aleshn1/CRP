from django.contrib.admin import action
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver
from django.urls import reverse

from crp import settings
from .models import Membros, Historico
from ..pastorais.models import Pastorais

user = settings.AUTH_USER_MODEL


@receiver(post_save, sender=Membros)
def registrar_mudanca_pastoral_elo(sender, instance, **kwargs):
    if instance._state.adding:  
        return

    if instance.pk:
        membro_anterior = Membros.objects.get(pk=instance.pk)
        if membro_anterior.pastorais.all() != instance.pastorais.all() or membro_anterior.elo != instance.elo:
            userlogged = instance.user
            pastorais_atuais = instance.pastorais.all()  

            
            if (membro_anterior.pastorais.all() != instance.pastorais.all() or
                    membro_anterior.elo != instance.elo):
                historico = Historico.objects.create(
                    membro=instance,
                    nova_pastoral=instance.pastorais.last(),
                    novo_elo=instance.get_elo_display(),
                    usuario=userlogged,
                )
                historico.pastorais_atuais.set(pastorais_atuais)


@receiver(m2m_changed, sender=Membros.pastorais.through)
def registrar_pastorais_adicionadas_removidas(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == 'pre_remove':
        pastorais_removidas = Pastorais.objects.filter(id__in=pk_set)

        
        if pastorais_removidas.exists():
            historico = Historico.objects.create(
                membro=instance,
                novo_elo=instance.get_elo_display(),
                usuario=instance.user,
            )
            historico.pastorais_removidas.set(pastorais_removidas)

            pastorais_atuais = instance.pastorais.exclude(id__in=pk_set)
            historico.pastorais_atuais.clear()
            historico.pastorais_atuais.add(*pastorais_atuais)
    elif action == 'post_add':
        pastorais_adicionadas = instance.pastorais.filter(id__in=pk_set)

        if pastorais_adicionadas.exists():
            historico = Historico.objects.create(
                membro=instance,
                novo_elo=instance.get_elo_display(),
                usuario=instance.user,
            )
            historico.pastorais_adicionadas.set(pastorais_adicionadas)

            pastorais_atuais = instance.pastorais.all()
            historico.pastorais_atuais.clear()
            historico.pastorais_atuais.add(*pastorais_atuais)
