from django.contrib import admin
from django.utils.html import format_html

from apps.elos.models import Elos


@admin.register(Elos)
class ElosAdmin(admin.ModelAdmin):
    list_display = ['nome', ]
    fields = ('nome',)

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)

        if db_field.name == 'nome' and formfield.required:
            formfield.label = format_html('{} <span style="color:red;">*</span>', formfield.label)

        return formfield
