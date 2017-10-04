# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-02 23:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='empleado',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='web.Empleado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='show',
            name='equipo',
            field=models.ForeignKey(default=django.utils.timezone.now, on_delete=django.db.models.deletion.CASCADE, to='web.Equipo'),
            preserve_default=False,
        ),
    ]