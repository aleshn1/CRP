# Generated by Django 4.2.4 on 2023-08-20 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voluntarios', '0003_voluntarios_sexo_remove_voluntarios_pastorais_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='voluntarios',
            options={'verbose_name': 'Voluntario', 'verbose_name_plural': 'Voluntarios'},
        ),
    ]
