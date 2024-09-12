# -*- encoding: utf-8 -*-

from django import forms
from django.contrib.auth import authenticate

from apps.members.models import Membros, Profession


class LoginForm(forms.Form):

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(LoginForm, self).__init__(*args, **kwargs)

    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))

    def clean(self):
        msg = "Email ou senha inválidos."
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        user = authenticate(username=email, password=password)
        if not user:
            raise forms.ValidationError(msg)
        return cleaned_data

    def get_user(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            user = authenticate(request=self.request, username=email, password=password)
            if user:
                return user


class UserUpdateData(forms.ModelForm):
    class Meta:
        model = Membros
        exclude = ['dt_nascimento', 'email', 'nome_completo', 'cpf', 'sexo']

    telefone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Telefone",
                "class": "form-control",
                "id": "celular"
            }
        ))
    celular = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Celular",
                "class": "form-control",
                "id": "celular"
            }
        ))

    marital_status = forms.ChoiceField(
        widget=forms.Select(attrs={
            "placeholder": "Estado Civil",
            "class": "form-control",
            "id": "profession"
        }),
        required=False,
        choices=Membros.marital_status_choices
    )

    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Endereço",
                "class": "form-control",
                "id": "address"
            }
        ))
    neighborhood = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Bairro",
                "class": "form-control",
                "id": "neighborhood"
            }
        ))
    city = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Cidade",
                "class": "form-control",
                "id": "city"
            }
        ))
    state = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Estado",
                "class": "form-control",
                "id": "state"
            }
        ))
    cep = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Cep",
                "class": "form-control",
                "id": "cep"
            }
        ))
    conjugue = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "cônjuge",
                "class": "form-control",
                "id": "conjugue"
            }

        ),
        required=False
    )

    profession = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={
                "placeholder": "Profissão",
                "class": "form-control",
                "id": "profession"
            }
        ),
        required=False,
        label=True,
        queryset=Profession.objects.all(),

    )
    igreja = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Igreja",
                "class": "form-control",
                "id": "parish"
            }
        ),
        required=False,
    )

    is_retired = forms.BooleanField(
        required=False
    )

    imagem_perfil = forms.FileField(
        label='Profile Image',
        required=False,
        widget=forms.FileInput(
            attrs={
                'class': 'form-control',
                'accept': 'image/png, image/jpeg',
                'type': "file",
            }
        ),
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

        if user:
            self.fields['imagem_perfil'].widget.attrs.update({'accept': '*', 'data-target': "_blank"})
