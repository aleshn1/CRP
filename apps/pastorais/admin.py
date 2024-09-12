from django.contrib import admin
from django.utils.html import format_html

from apps.pastorais.models import Pastorais


@admin.register(Pastorais)
class PastoraisAdmin(admin.ModelAdmin):
    class Meta:
        model = Pastorais
        fields = '__all__'
        extra = 1
        list_display = ("nome",)
        list_filter = ("pastorais",)
        verbose_name = 'Pastoral'
        verbose_name_plural = 'Pastorais'

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)
        required_fields = ['nome', ]
        if db_field.name in required_fields and formfield.required:
            formfield.label = format_html('{} <span style="color:red;">*</span>', formfield.label)

        return formfield
