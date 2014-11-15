# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('referrals', '0002_auto_20141019_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='referral',
            name='description',
            field=models.CharField(default=b'', max_length=1000),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='referral',
            name='uuid',
            field=models.CharField(default=datetime.date(2014, 10, 28), max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='referral',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='referral',
            name='time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='level',
            field=models.IntegerField(default=1, choices=[(1, b'Teacher'), (2, b'Admin'), (3, b'Network Admin')]),
        ),
    ]
