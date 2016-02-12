# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-12 15:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('language', models.CharField(max_length=64)),
                ('filename', models.FileField(upload_to='books')),
            ],
        ),
        migrations.CreateModel(
            name='Paragraph',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index', models.IntegerField(unique=True)),
                ('paragraph', models.TextField()),
                ('recorded', models.BooleanField(default=False)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paragraphs', to='lyv.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Recording',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.FileField(upload_to='recordings')),
                ('paragraph', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='recordings', to='lyv.Paragraph')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_recording', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
