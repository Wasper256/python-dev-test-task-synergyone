# Generated by Django 2.1.5 on 2019-01-26 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('agreement_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crm.Application')),
            ],
        ),
    ]
