# Generated by Django 4.2.4 on 2023-08-25 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0011_delete_group_group'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Group',
        ),
    ]
