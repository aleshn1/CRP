from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render
from django.views.decorators.http import require_GET

from apps.members.models import Membros
from apps.pastorais.models import Pastorais


@login_required
@require_GET
def pastorais(request):
    filter_params = request.GET.get("search", "")

    pastorais_filter = Pastorais.objects.all().order_by("nome")
    pastorais_with_members = []

    if filter_params:
        pastorais_filter = pastorais_filter.filter(
            Q(nome__icontains=filter_params)
        )

    for pastoral in pastorais_filter:
        membros = Membros.objects.filter(pastorais__id=pastoral.id)
        membros_list = [{"name": membro.nome_completo, "elo": membro.get_elo_display()} for membro in
                        membros]
        membros_by_pastoral = {
            "pastoral": pastoral,
            "membros_count": membros.count(),
            "membros": membros_list

        }
        pastorais_with_members.append(membros_by_pastoral)
    context = {
        "pastorais": pastorais_with_members
    }

    return render(request, "pastorais/pastorais.html", context)
