# Generated by Django 2.0.1 on 2018-02-08 21:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0010_auto_20180207_1438'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empresa',
            options={'ordering': ['nome'], 'verbose_name_plural': 'Funcionários'},
        ),
    ]
