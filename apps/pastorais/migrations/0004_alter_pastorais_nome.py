# Generated by Django 4.2.4 on 2023-08-21 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastorais', '0003_rename_pastoral_pastorais_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pastorais',
            name='nome',
            field=models.CharField(choices=[('cozinha', 'Cozinha'), ('central de comunicacao', 'Central de comunicação'), ('lanchonete', 'Lanchonete(Quarta/Quinta)'), ('merce', 'Merce'), ('liturgia', 'Liturgia'), ('adoracao', 'Adoração'), ('limpeza', 'Limpeza'), ('loja', 'Loja'), ('bazar', 'Bazar'), ('sao cristovao', 'São Cristóvão'), ('apoio', 'Apoio'), ('intercessao', 'Intercessão'), ('sao miguel', 'São Miguel'), ('musicos', 'Músicos'), ('camarim', 'Camarim')], max_length=23),
        ),
    ]
