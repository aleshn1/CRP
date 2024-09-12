from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.

class Pastorais(models.Model):
    class Meta:
        verbose_name_plural = 'Pastorais'

    pastoral_choices = [
        ('cozinha', 'Cozinha'),
        ('central de comunicacao', 'Central de comunicação'),
        ('lanchonete', 'Lanchonete(Quarta/Quinta)'),
        ('merce', 'Mercê'),
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
        ('revista', 'Revista'),
        ('pastoral de rua', 'Pastoral de Rua'),
        ('conselho do 3º elo', 'Conselho do 3º Elo'),
        ('conselho geral', 'Conselho Geral'),
        ('formadora geral', 'Formadora Geral'),
    ]
    nome = models.CharField(max_length=23, null=False, blank=False, choices=pastoral_choices)

    def __str__(self):
        return self.get_nome_display()

    def clean(self):
        
        existing_pastorais = Pastorais.objects.filter(nome=self.nome).exclude(id=self.id)
        if existing_pastorais.exists():
            raise ValidationError('Esta pastoral já foi adicionada.')

    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)
