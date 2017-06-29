# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 12:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=20000, verbose_name='Tweet Content')),
                ('published_at', models.DateTimeField(verbose_name='Published At')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Last Update')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
            ],
            options={
                'verbose_name': 'Tweet',
                'verbose_name_plural': 'Tweets',
            },
        ),
    ]