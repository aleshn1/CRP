from django import forms

from apps.vocacionados.models import Vocacionados


class VocacionadosFormAdmin(forms.ModelForm):
    class Meta:
        model = Vocacionados
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs['class'] = 'cpf'
        self.fields['cep'].widget.attrs['class'] = 'cep'
        self.fields['celular'].widget.attrs['class'] = 'celular'
        self.fields['telefone'].widget.attrs['class'] = 'telefone'
        self.fields['data_entrada'].widget.attrs['class'] = 'dt_entrada'
        self.fields['data_nascimento'].widget.attrs['class'] = 'dt_nascimento'
        self.fields['data_matrimonio'].widget.attrs['class'] = 'dt_matrimonio'
