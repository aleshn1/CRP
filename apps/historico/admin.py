from django.contrib import admin

from apps.historico.models import Historico


@admin.register(Historico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('membro', 'novo_elo', 'nova_pastoral', 'data_mudanca', 'usuario')
    list_filter = ('membro__nome_completo', 'novo_elo', 'nova_pastoral', 'usuario')
    search_fields = ('membro__nome_completo', 'novo_elo', 'nova_pastoral', 'usuario__username')
    list_per_page = 20
    ordering = ('-data_mudanca',)
