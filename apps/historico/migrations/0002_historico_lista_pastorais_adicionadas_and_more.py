# Generated by Django 4.2.4 on 2023-08-28 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('historico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='historico',
            name='lista_pastorais_adicionadas',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='historico',
            name='lista_pastorais_removidas',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
