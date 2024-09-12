from django.contrib import admin
from django.utils.html import format_html

from apps.vocacionados.forms import VocacionadosFormAdmin
from apps.vocacionados.models import Vocacionados


@admin.register(Vocacionados)
class VocacionadosAdmin(admin.ModelAdmin):
    form = VocacionadosFormAdmin
    filter_horizontal = ['pastorais']

    class Meta:
        model = Vocacionados
        fields = '__all__'

    list_display = ['nome_completo', 'email', 'telefone', 'celular', 'cpf', 'sexo', 'data_entrada']

    fieldsets = [
        (None, {'fields': ('nome_completo', 'data_nascimento', 'cpf', 'sexo')}),
        ('Contato', {'fields': ('telefone', 'celular', 'email')}),
        ('Endereço', {'fields': ('cep', 'endereco', 'cidade', 'bairro', 'estado')}),
        ('Estado Civil', {'fields': ('estado_civil', 'data_matrimonio', 'conjugue')}),
        ('Profissional', {'fields': ('profissao', 'formacao_academica', 'aposentado',)}),
        ('CRP', {'fields': ('orientador', 'pastorais', 'data_entrada')}),
        ('Outros', {'fields': ('foto',)}),
    ]
    search_fields = ('nome_completo', 'cpf', 'email')

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        required_fields = ['nome_completo', 'data_nascimento', 'celular', 'cpf', 'sexo', 'estado_civil']
        if db_field.name in required_fields and formfield.required:
            formfield.label = format_html('{} <span style="color:red;">*</span>', formfield.label)

        return formfield

    class Media:
        js = ('assets/js/jquery.mask.min.js',
              'assets/js/admin_custom.js',
              )
