from django import forms

from apps.members.models import Membros


class MembrosFormAdmin(forms.ModelForm):
    class Meta:
        model = Membros
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cpf'].widget.attrs['class'] = 'cpf'
        self.fields['cep'].widget.attrs['class'] = 'cep'
        self.fields['celular'].widget.attrs['class'] = 'celular'
        self.fields['telefone'].widget.attrs['class'] = 'telefone'
        self.fields['falecido'].widget.attrs['class'] = 'falecido'
        self.fields['dt_promessa'].widget.attrs['class'] = 'dt_promessa'
        self.fields['dt_nascimento'].widget.attrs['class'] = 'dt_nascimento'
        self.fields['dt_matrimonio'].widget.attrs['class'] = 'dt_matrimonio'
        self.fields['atestado_obito'].widget.attrs['class'] = 'atestado_obito'
