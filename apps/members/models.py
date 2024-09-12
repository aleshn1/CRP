from django.core.exceptions import ValidationError
from django.db import models

from apps.pastorais.models import Pastorais
from crp import settings

class Profession(models.Model):
    class Meta:
        ordering = ['name']
        db_table = 'Profession'
        verbose_name = 'Profissão'
        verbose_name_plural = 'Profissões'

    name = models.CharField(max_length=255, null=False, blank=False, verbose_name='Profissão')
    updateAt = models.DateTimeField(null=False, blank=False, editable=False, auto_now=True)
    createAt = models.DateTimeField(null=False, blank=False, editable=False, auto_now_add=True)

    def __str__(self):
        return self.name

    def clean(self):
        # Check for duplicate elos with the same nome
        existing_profession = Profession.objects.filter(name=self.name).exclude(id=self.id)
        if existing_profession.exists():
            raise ValidationError('Esta Profissão já foi cadastrado(a).')

    def save(self, *args, **kwargs):
        self.full_clean()  # Run full validation before saving
        super().save(*args, **kwargs)


class Membros(models.Model):
    class Meta:
        verbose_name_plural = 'Membros'
        verbose_name = 'Membro'

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, null=True, blank=True,
                                verbose_name='Usuario')
    nome_completo = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome Completo')
    dt_nascimento = models.DateField(null=False, blank=False, verbose_name='Data de Nascimento')
    cpf = models.CharField(max_length=14, null=False, blank=False, verbose_name='CPF')
    sexo_choices = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    ]
    sexo = models.CharField(max_length=1, null=False, blank=False, choices=sexo_choices, verbose_name='Sexo')
    telefone = models.CharField(max_length=20, null=True, blank=True, verbose_name='Telefone')
    celular = models.CharField(max_length=20, null=False, blank=False, verbose_name='Celular')
    email = models.EmailField(null=False, blank=False, verbose_name='Email')
    observacao = models.TextField(max_length=500, null=True, blank=True, verbose_name='Observação')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='Endereço')
    neighborhood = models.CharField(max_length=50, null=True, blank=True, verbose_name='Bairro')
    city = models.CharField(max_length=50, null=True, blank=True, verbose_name='Cidade')
    state = models.CharField(max_length=50, null=True, blank=True, verbose_name='Estado')
    cep = models.CharField(max_length=10, null=True, blank=True, verbose_name='CEP')
    conjugue = models.CharField(max_length=200, null=True, blank=True, verbose_name='Conjugue')
    marital_status_choices = [
        ('Solteiro', 'Solteiro'),
        ('Casado', 'Casado'),
        ('Separado', 'Separado'),
        ('Divorciado', 'Divorciado'),
        ('Viuvo', 'Viúvo'),
    ]
    estado_civil = models.CharField(max_length=20, null=False, blank=False, choices=marital_status_choices,
                                    verbose_name='Estado Civil')
    profession = models.ForeignKey(Profession, on_delete=models.CASCADE, blank=True, null=True,
                                   verbose_name='Profissão')
    aposentado = models.BooleanField(default=False, null=True, blank=True, verbose_name='Aposentado')
    afastado = models.BooleanField(default=False, null=True, blank=True, verbose_name='Afastado')
    falecido = models.BooleanField(default=False, null=True, blank=True, verbose_name='Falecido')
    atestado_obito = models.FileField(upload_to='atestado_obito/%d-%m-%Y', blank=True, null=True, verbose_name='Atestado de Obito')
    education_choices = [
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

    education = models.CharField(max_length=22, null=True, blank=True, choices=education_choices,
                                 verbose_name='Formação')
    dt_promessa = models.DateField(null=True, blank=True, verbose_name='Data da Promessa')
    dt_matrimonio = models.DateField(null=True, blank=True, verbose_name='Data do Matrimonio')
    mentor = models.CharField(max_length=255, null=True, blank=True, verbose_name='Orientador(a)')
    imagem_perfil = models.ImageField(upload_to='profile_images/%d-%m-%Y', blank=True, null=True)
    pastorais = models.ManyToManyField(Pastorais, related_name='membros',
                                       verbose_name='Pastorais', blank=True)
    elo_choices = [
        ('1_elo', '1º elo'),
        ('2_elo', '2º elo'),
        ('3_elo', '3º elo'),
    ]

    elo = models.CharField(max_length=50, null=False, blank=False, choices=elo_choices)
    criadoEm = models.DateTimeField(null=False, blank=False, editable=False,
                                    auto_now_add=True,
                                    verbose_name='Criado Em')
    atualizadoEm = models.DateTimeField(null=False, blank=False, editable=False,
                                        auto_now=True,
                                        verbose_name='Atualizado Em')

    def __str__(self):
        return f'{self.nome_completo} '


class Formadores(models.Model):
    class Meta:
        verbose_name = 'Formador'
        verbose_name_plural = 'Formadores'

    nome = models.CharField(max_length=255, null=False, blank=False, verbose_name='Nome')
    membro = models.ManyToManyField(Membros, related_name='formadores',
                                    verbose_name='Membro Associado', blank=True)

    def __str__(self):
        return f'{self.nome} ({self.membro.count()} membros associados)'
