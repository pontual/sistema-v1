# Generated by Django 2.0.1 on 2018-02-02 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0004_auto_20180202_2310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='products/'),
        ),
    ]
