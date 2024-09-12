from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import render
from django.views.decorators.http import require_GET

from apps.historico.models import Historico


@login_required
@require_GET
def historico(request):
    historicos = Historico.objects.all().order_by('-data_mudanca')

    filter_params = request.GET.get("search", "")
    if filter_params:

        historicos = historicos.filter(
            Q(membro__nome_completo__icontains=filter_params)
        )
    else:
        historicos = historicos.order_by("membro")
    paginator = Paginator(historicos, 10)
    page = request.GET.get('page', 1)
    try:
        historicos_paginados = paginator.page(page)
    except PageNotAnInteger:
        historicos_paginados = paginator.page(1)
    except EmptyPage:
        historicos_paginados = paginator.page(paginator.num_pages)

    return render(request, 'historico/historicos.html', {'historicos': historicos_paginados})
