# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-07-29 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrowseNotes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_id', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F')], max_length=1)),
                ('purpose', models.TextField()),
                ('term', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='LoanStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_id', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('funded_amount', models.IntegerField()),
                ('purpose', models.TextField()),
            ],
        ),
    ]