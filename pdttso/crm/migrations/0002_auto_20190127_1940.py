# Generated by Django 2.1.5 on 2019-01-27 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='agreement_id',
            field=models.IntegerField(unique=True),
        ),
    ]