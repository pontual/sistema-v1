# Generated by Django 2.0.1 on 2018-02-08 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0011_auto_20180208_2108'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empresa',
            options={'ordering': ['nome']},
        ),
        migrations.AlterModelOptions(
            name='funcionario',
            options={'ordering': ['user__username'], 'verbose_name_plural': 'Funcionários'},
        ),
    ]
