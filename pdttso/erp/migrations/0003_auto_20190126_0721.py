# Generated by Django 2.1.5 on 2019-01-26 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
        ('erp', '0002_auto_20190126_0653'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Payments',
            new_name='Payment',
        ),
    ]
