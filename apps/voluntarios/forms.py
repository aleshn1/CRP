from django import forms

from apps.vocacionados.models import Vocacionados
from apps.voluntarios.models import Voluntarios


class VoluntariosFormAdmin(forms.ModelForm):
    class Meta:
        model = Voluntarios
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['celular'].widget.attrs['class'] = 'celular'
        self.fields['telefone'].widget.attrs['class'] = 'telefone'
        self.fields['data_nascimento'].widget.attrs['class'] = 'dt_nascimento'
