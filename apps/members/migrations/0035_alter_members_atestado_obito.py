# Generated by Django 4.2.4 on 2023-08-14 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0034_alter_members_aposentado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='members',
            name='atestado_obito',
            field=models.FileField(blank=True, null=True, upload_to='atestado_obito/%d-%m-%Y', verbose_name='Atestado de Obito'),
        ),
    ]
