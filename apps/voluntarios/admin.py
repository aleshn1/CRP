from django.contrib import admin
from django.utils.html import format_html

from apps.voluntarios.forms import VoluntariosFormAdmin
from apps.voluntarios.models import Voluntarios


@admin.register(Voluntarios)
class VoluntariosAdmin(admin.ModelAdmin):
    form = VoluntariosFormAdmin
    filter_horizontal = ['pastorais']

    class Meta:
        model = Voluntarios
        fields = '__all__'

    list_display = ['nome_completo', 'email', 'telefone', 'celular', 'sexo']

    fieldsets = [
        (None, {'fields': ('nome_completo', 'data_nascimento', 'sexo')}),
        ('Contato', {'fields': ('telefone', 'celular', 'email')}),
        ('CRP', {'fields': ('pastorais',)}),
    ]
    search_fields = ('nome_completo', 'cpf', 'email')

    class Media:
        js = ('assets/js/jquery.mask.min.js',
              'assets/js/admin_custom.js',
              )

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        required_fields = ['nome_completo','data_nascimento', 'sexo', 'email', 'telefone', 'celular', ]
        if db_field.name in required_fields and formfield.required:
            formfield.label = format_html('{} <span style="color:red;">*</span>', formfield.label)

        return formfield
