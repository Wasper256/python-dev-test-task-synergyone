# Generated by Django 2.1.5 on 2019-01-27 19:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0003_auto_20190126_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='agreement_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Application', to_field='agreement_id'),
        ),
    ]
