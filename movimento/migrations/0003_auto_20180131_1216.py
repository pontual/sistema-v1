# Generated by Django 2.0.1 on 2018-01-31 14:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movimento', '0002_auto_20180130_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='comprador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='empresa_compradora', to='registros.Empresa'),
        ),
        migrations.AlterField(
            model_name='transacao',
            name='vendedor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='empresa_vendedora', to='registros.Empresa'),
        ),
    ]