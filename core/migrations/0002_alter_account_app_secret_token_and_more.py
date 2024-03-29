# Generated by Django 5.0.2 on 2024-02-15 07:23

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='app_secret_token',
            field=models.CharField(default=uuid.uuid4, max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='destination',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.account'),
        ),
        migrations.AlterField(
            model_name='destination',
            name='headers',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='destination',
            name='http_method',
            field=models.CharField(choices=[('GET', 'GET'), ('POST', 'POST'), ('PUT', 'PUT')], max_length=10),
        ),
    ]
