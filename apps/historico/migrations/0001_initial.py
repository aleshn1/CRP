# Generated by Django 4.2.4 on 2023-08-28 11:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0050_alter_membros_pastorais'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pastorais', '0006_alter_pastorais_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Historico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('novo_elo', models.CharField(max_length=50)),
                ('data_mudanca', models.DateTimeField(auto_now_add=True)),
                ('membro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='members.membros')),
                ('nova_pastoral', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='pastorais.pastorais')),
                ('usuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
