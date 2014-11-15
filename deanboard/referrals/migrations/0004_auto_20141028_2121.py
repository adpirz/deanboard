# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('referrals', '0003_auto_20141028_2055'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='referral',
            name='date',
        ),
        migrations.RemoveField(
            model_name='referral',
            name='time',
        ),
        migrations.RemoveField(
            model_name='referral',
            name='uuid',
        ),
        migrations.RemoveField(
            model_name='scholar',
            name='id',
        ),
        migrations.AddField(
            model_name='referral',
            name='datetime',
            field=models.DateTimeField(default=datetime.date(2014, 10, 28), auto_now=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='scholar',
            name='kbid',
            field=models.IntegerField(unique=True, serialize=False, primary_key=True),
        ),
    ]
