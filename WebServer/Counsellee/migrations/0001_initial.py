# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-02 05:49
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
            name='CounselleeDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateOfBirth', models.DateField()),
                ('address', models.CharField(max_length=1000)),
                ('uid', models.BigIntegerField()),
                ('phoneNo', models.BigIntegerField()),
                ('gender', models.CharField(max_length=6)),
                ('role', models.CharField(default='Counsellee', max_length=10)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
