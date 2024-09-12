from django.db import models

from apps.pastorais.models import Pastorais


# Create your models here.
class Voluntarios(models.Model):
    class Meta:
        verbose_name = 'Voluntario'
        verbose_name_plural = 'Voluntarios'

    nome_completo = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome Completo')
    data_nascimento = models.DateField(null=False, blank=False, verbose_name='Data de Nascimento')
    telefone = models.CharField(max_length=20, null=False, blank=False, verbose_name='Telefone')
    celular = models.CharField(max_length=20, null=False, blank=False, verbose_name='Celular')
    sexo_choices = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    sexo = models.CharField(max_length=1, null=False, blank=False, choices=sexo_choices, verbose_name='Sexo')
    email = models.EmailField(null=True, blank=True, verbose_name='Email')
    data_entrada = models.DateField(null=True, blank=True, verbose_name='Data de Entrada')
    
    pastoral_choices = [
        ('cozinha', 'Cozinha'),
        ('central de comunicacao', 'Central de comunicação'),
        ('lanchonete', 'Lanchonete(Quarta/Quinta)'),
        ('merce', 'Merce'),
        ('liturgia', 'Liturgia'),
        ('adoracao', 'Adoração'),
        ('limpeza', 'Limpeza'),
        ('loja', 'Loja'),
        ('bazar', 'Bazar'),
        ('sao cristovao', 'São Cristóvão'),
        ('apoio', 'Apoio'),
        ('intercessao', 'Intercessão'),
        ('sao miguel', 'São Miguel'),
        ('musicos', 'Músicos'),
        ('camarim', 'Camarim'),
    ]
    pastorais = models.ManyToManyField(Pastorais, related_name='voluntarios_pastorais',
                                       verbose_name='Pastorais', blank=True)
    criado_em = models.DateTimeField(null=False, blank=False, editable=False,
                                     auto_now_add=True,
                                     verbose_name='Criado Em'),
    atualizado_em = models.DateTimeField(null=False, blank=False, editable=False,
                                         auto_now=True,
                                         verbose_name='Atualizado Em')

    def __str__(self):
        return self.nome_completo
