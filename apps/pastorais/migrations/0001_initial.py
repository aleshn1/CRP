# Generated by Django 4.1.10 on 2023-08-08 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('members', '0019_remove_members_pastorais'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pastorais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pastoral', models.CharField(blank=True, choices=[('cozinha', 'Cozinha'), ('central de comunicacao', 'Central de comunicação'), ('lanchonete', 'Lanchonete(Quarta/Quinta)'), ('merce', 'Merce'), ('liturgia', 'Liturgia'), ('adoracao', 'Adoração'), ('limpeza', 'Limpeza'), ('loja', 'Loja'), ('bazar', 'Bazar'), ('sao cristovao', 'São Cristóvão'), ('apoio', 'Apoio'), ('intercessao', 'Intercessão'), ('sao miguel', 'São Miguel'), ('musicos', 'Músicos'), ('camarim', 'Camarim')], max_length=23, null=True)),
                ('member', models.ManyToManyField(blank=True, related_name='pastoral', to='members.members', verbose_name='Membro Associado')),
            ],
        ),
    ]
