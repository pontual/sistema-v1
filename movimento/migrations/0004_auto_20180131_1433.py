# Generated by Django 2.0.1 on 2018-01-31 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movimento', '0003_auto_20180131_1216'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transacao',
            old_name='date_recorded',
            new_name='data',
        ),
    ]
