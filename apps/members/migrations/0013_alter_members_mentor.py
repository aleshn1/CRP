# Generated by Django 4.1.10 on 2023-08-01 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0012_members_pastorais_alter_members_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='mentor',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Orientador(a)'),
        ),
    ]
