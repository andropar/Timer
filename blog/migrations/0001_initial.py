# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-17 10:13
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateField()),
                ('content', tinymce.models.HTMLField()),
            ],
        ),
    ]