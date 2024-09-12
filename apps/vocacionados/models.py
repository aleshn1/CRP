from django.db import models

from apps.members.models import Profession
from apps.pastorais.models import Pastorais


class Vocacionados(models.Model):
    class Meta:
        verbose_name = 'Vocacionado'
        verbose_name_plural = 'Vocacionados'

    nome_completo = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome Completo')
    data_nascimento = models.DateField(null=False, blank=False, verbose_name='Data de Nascimento')
    cpf = models.CharField(max_length=14, null=False, blank=False, verbose_name='CPF')
    sexo_choices = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    sexo = models.CharField(max_length=1, null=False, blank=False, choices=sexo_choices, verbose_name='Sexo')
    telefone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Telefone')
    celular = models.CharField(max_length=20, null=False, blank=False, verbose_name='Celular')
    email = models.EmailField(null=True, blank=True, verbose_name='Email')
    observacao = models.TextField(max_length=500, null=True, blank=True, verbose_name='Observação')
    endereco = models.CharField(max_length=255, null=True, blank=True, verbose_name='Endereço')
    bairro = models.CharField(max_length=50, null=True, blank=True, verbose_name='Bairro')
    cidade = models.CharField(max_length=50, null=True, blank=True, verbose_name='Cidade')
    estado = models.CharField(max_length=50, null=True, blank=True, verbose_name='Estado')
    cep = models.CharField(max_length=10, null=True, blank=True, verbose_name='CEP')
    conjugue = models.CharField(max_length=200, null=True, blank=True, verbose_name='Conjugue')
    estado_civil_choices = [
        ('Solteiro', 'Solteiro'),
        ('Casado', 'Casado'),
        ('Separado', 'Separado'),
        ('Divorciado', 'Divorciado'),
        ('Viuvo', 'Viúvo'),
    ]
    estado_civil = models.CharField(max_length=20, null=False, blank=False, choices=estado_civil_choices,
                                    verbose_name='Estado Civil')
    profissao = models.ForeignKey(Profession, on_delete=models.CASCADE, blank=True, null=True,
                                  verbose_name='Profissão')
    aposentado = models.BooleanField(default=False, null=False, blank=False, verbose_name='Aposentado')
    formacao_academica_choices = [
        ('aprendizado_online', 'Aprendizado Online'),
        ('bacharelado', 'Bacharelado'),
        ('doutorado', 'Doutorado'),
        ('educacao_continuada', 'Educação Continuada'),
        ('ensino fundamental', 'Ensino Fundamental'),
        ('ensino medio', 'Ensino Médio'),
        ('especializacao', 'Especialização'),
        ('graduacao', 'Graduação'),
        ('licenciatura', 'Licenciatura'),
        ('mestrado', 'Mestrado'),
        ('mba', 'MBA (Master of Business Administration)'),
        ('phd', 'Ph.D.'),
        ('pos-graduacao', 'Pós-graduação'),
        ('tecnico', 'Técnico'),
        ('tecnologo', 'Tecnologo'),
    ]

    formacao_academica = models.CharField(max_length=22, null=True, blank=True, choices=formacao_academica_choices,
                                          verbose_name='Formação Acadêmica')
    data_matrimonio = models.DateField(null=True, blank=True, verbose_name='Data do Matrimonio')
    orientador = models.CharField(max_length=255, null=True, blank=True, verbose_name='Orientador(a)')
    foto = models.ImageField(upload_to='fotos_vocacionados/%d-%m-%Y', blank=True, null=True)
    pastorais = models.ManyToManyField(Pastorais, related_name='vocacionados_pastorais',
                                       verbose_name='Pastorais', blank=True)
    data_entrada = models.DateField(null=True, blank=True, verbose_name='Data de entrada')
    criado_em = models.DateTimeField(null=False, blank=False, editable=False,
                                     auto_now_add=True,
                                     verbose_name='Criado Em'),
    atualizado_em = models.DateTimeField(null=False, blank=False, editable=False,
                                         auto_now=True,
                                         verbose_name='Atualizado Em')

    def __str__(self):
        return self.nome_completo
