from django import forms

from apps.pastorais.models import Pastorais


class PastoraisFormAdmin(forms.ModelForm):
    class Meta:
        model = Pastorais
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].queryset = Pastorais.objects.all()
