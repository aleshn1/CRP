# Generated by Django 4.2.4 on 2023-08-20 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastorais', '0003_rename_pastoral_pastorais_nome'),
        ('vocacionados', '0005_alter_vocacionados_pastorais'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vocacionados',
            name='pastorais',
        ),
        migrations.AddField(
            model_name='vocacionados',
            name='pastorais',
            field=models.ManyToManyField(blank=True, related_name='vocacionados_pastorais', to='pastorais.pastorais', verbose_name='Pastorais'),
        ),
    ]
