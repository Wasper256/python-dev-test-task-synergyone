# Generated by Django 2.1.5 on 2019-01-26 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=30),
        ),
    ]
