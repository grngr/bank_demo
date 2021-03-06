# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fund_transfer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeraccount',
            name='account_type',
            field=models.CharField(choices=[('sa', 'Savings'), ('ca', 'Current'), ('cc', 'Credit Card')], default='s', max_length=1),
        ),
        migrations.AlterField(
            model_name='payee',
            name='account_type',
            field=models.CharField(choices=[('sa', 'Savings'), ('ca', 'Current'), ('cc', 'Credit Card')], default='sa', help_text='Please choose the account / card type', max_length=2, verbose_name='Account / Card type'),
        ),
    ]
