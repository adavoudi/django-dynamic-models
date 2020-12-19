# Generated by Django 3.1.4 on 2020-12-19 14:37

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic_models', '0002_remove_modelschema__modified'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fieldschema',
            name='data_type',
        ),
        migrations.RemoveField(
            model_name='fieldschema',
            name='max_length',
        ),
        migrations.RemoveField(
            model_name='fieldschema',
            name='unique',
        ),
        migrations.AddField(
            model_name='fieldschema',
            name='class_name',
            field=models.TextField(default=""),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='fieldschema',
            name='kwargs',
            field=django.contrib.postgres.fields.jsonb.JSONField(default=dict),
        ),
    ]