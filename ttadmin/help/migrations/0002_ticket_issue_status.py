# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-19 23:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('help', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='issue_status',
            field=models.CharField(choices=[('triage', 'to triage'), ('acked', 'acknowledged'), ('waiting', 'waiting to hear from submitter'), ('completed', 'nothing more to do')], default='triage', max_length=50),
        ),
    ]
