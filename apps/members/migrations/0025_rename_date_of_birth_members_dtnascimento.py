# Generated by Django 4.2.4 on 2023-08-11 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0024_members_updateat'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='date_of_birth',
            new_name='dtNascimento',
        ),
    ]
