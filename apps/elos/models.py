from django.core.exceptions import ValidationError
from django.db import models

class Elos(models.Model):
    class Meta:
        verbose_name = "Elo"
        verbose_name_plural = "Elos"

    elo_choices = [
        ('1_elo', '1º elo'),
        ('2_elo', '2º elo'),
        ('3_elo', '3º elo'),
    ]
    nome = models.CharField(max_length=23, null=False, blank=False, choices=elo_choices)

    def __str__(self):
        return self.nome

    def clean(self):
        
        existing_elo = Elos.objects.filter(nome=self.nome).exclude(id=self.id)
        if existing_elo.exists():
            raise ValidationError('Este elo já foi adicionado.')

    def save(self, *args, **kwargs):
        self.full_clean()  
        super().save(*args, **kwargs)
