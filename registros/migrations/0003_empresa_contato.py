# Generated by Django 2.0.1 on 2018-02-02 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0002_auto_20180130_2339'),
    ]

    operations = [
        migrations.AddField(
            model_name='empresa',
            name='contato',
            field=models.CharField(blank=True, max_length=63),
        ),
    ]
