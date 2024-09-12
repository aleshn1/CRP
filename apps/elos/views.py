import logging

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.http import require_GET

from apps.elos.models import Elos
from apps.members.models import Membros


@login_required
@require_GET
def elos(request):
    logging.info('Iniciando listagem de elos...')

    elos_list = Elos.objects.all().order_by("nome")
    elos_with_members = []

    for elo in elos_list:
        membros = Membros.objects.filter(elo=elo)
        membros_list = [{"name": membro.nome_completo} for membro in membros]
        elos_by_members = {
            "elo": elo,
            "membros_count": membros.count(),
            "membros": membros_list
        }
        elos_with_members.append(elos_by_members)

    context = {
        "elos": elos_with_members
    }
    logging.info('Elos carregados com sucesso!')
    return render(request, "elos/elos.html", context)
