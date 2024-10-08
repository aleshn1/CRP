# Generated by Django 4.2.4 on 2023-08-23 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0050_alter_membros_pastorais'),
        ('elos', '0003_alter_elos_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='elos',
            name='membro',
            field=models.ManyToManyField(blank=True, related_name='elos', to='members.membros', verbose_name='Membro Associado'),
        ),
    ]
