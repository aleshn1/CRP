from django.contrib import admin
from django.utils.html import format_html

from apps.members.forms import MembrosFormAdmin
from apps.members.models import Membros, Profession, Formadores


class TrainersInline(admin.TabularInline):
    model = Membros.formadores.through
    extra = 1
    list_display = ["name"]
    list_filter = ("name",)
    verbose_name = 'Formador'

    verbose_name_plural = 'Formadores'
    raw_id_fields = ("membros",)


@admin.register(Membros)
class MembersAdmin(admin.ModelAdmin):
    form = MembrosFormAdmin
    filter_horizontal = ['pastorais']

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        required_fields = ['nome_completo', 'dt_nascimento', 'cpf', 'sexo', 'celular', 'email', 'estado_civil', 'elo', ]
        if db_field.name in required_fields and formfield.required:
            formfield.label = format_html('{} <span style="color:red;">*</span>', formfield.label)

        return formfield

    class Meta:
        verbose_name_plural = "Membros"
        model = Membros
        fields = '__all__'

    class Media:
        js = ('assets/js/jquery.mask.min.js',
              'assets/js/admin_custom.js',
              )

    inlines = [TrainersInline]

    list_display = ['nome_completo', 'email', 'telefone', 'celular', 'cpf', 'sexo', 'elo']
    fieldsets = [
        (None, {'fields': ('user', 'nome_completo', 'dt_nascimento', 'cpf', 'sexo')}),
        ('Contato', {'fields': ('telefone', 'celular', 'email')}),
        ('Endereço', {'fields': ('cep', 'address', 'city', 'neighborhood', 'state')}),
        ('Estado Civil', {'fields': ('estado_civil', 'dt_matrimonio', 'conjugue')}),
        ('Profissional', {'fields': ('profession', 'education', 'aposentado',)}),
        ('CRP', {'fields': ('dt_promessa', 'mentor', 'pastorais', 'elo')}),
        ('Outros', {'fields': ('observacao', 'imagem_perfil', 'afastado', 'falecido', 'atestado_obito')}),
    ]
    search_fields = ('nome_completo', 'elo', 'email')


def formfield_for_dbfield(self, db_field, **kwargs):
    formfield = super().formfield_for_dbfield(db_field, **kwargs)
    required_fields = ['nome_completo', 'dt_nascimento', 'cpf', 'sexo', 'celular', 'email', 'estado_civil', 'elo', ]
    if db_field.name in required_fields and formfield.required:
        formfield.label = format_html('{} <span style="color:red;">*</span>', formfield.label)

    return formfield


@admin.register(Formadores)
class FormadoresAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        required_fields = ['nome', ]
        if db_field.name in required_fields and formfield.required:
            formfield.label = format_html('{} <span style="color:red;">*</span>', formfield.label)

        return formfield


@admin.register(Profession)
class ProfessionAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        required_fields = ['name', ]
        if db_field.name in required_fields and formfield.required:
            formfield.label = format_html('{} <span style="color:red;">*</span>', formfield.label)

        return formfield
