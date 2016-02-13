# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-13 09:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lyv', '0002_auto_20160213_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(choices=[('Tamil', 'Tamil'), ('Punjabi', 'Punjabi'), ('Marathi', 'Marathi'), ('English', 'English'), ('Telugu', 'Telugu'), ('Hindi', 'Hindi'), ('Kannada', 'Kannada'), ('Bengali', 'Bengali')], max_length=64),
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='index',
            field=models.IntegerField(),
        ),
        migrations.AlterUniqueTogether(
            name='paragraph',
            unique_together=set([('book', 'index')]),
        ),
    ]
