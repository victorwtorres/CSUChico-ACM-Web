# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-15 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20160815_1015'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['-created']},
        ),
        migrations.AlterField(
            model_name='link',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='link',
            name='created',
            field=models.DateTimeField(),
        ),
    ]
