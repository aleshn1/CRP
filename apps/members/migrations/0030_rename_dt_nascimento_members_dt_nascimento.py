# Generated by Django 4.2.4 on 2023-08-11 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0029_rename_data_matrimonio_members_dt_matrimonio_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='dt_Nascimento',
            new_name='dt_nascimento',
        ),
    ]
