# Generated by Django 4.2.4 on 2023-08-20 11:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pastorais', '0003_rename_pastoral_pastorais_nome'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('members', '0048_alter_members_education_alter_members_telefone'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Members',
            new_name='Membros',
        ),
    ]
