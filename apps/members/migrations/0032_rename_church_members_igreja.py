# Generated by Django 4.2.4 on 2023-08-14 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0031_alter_members_pastorais'),
    ]

    operations = [
        migrations.RenameField(
            model_name='members',
            old_name='church',
            new_name='igreja',
        ),
    ]
