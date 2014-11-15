# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('referrals', '0004_auto_20141028_2121'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scholar',
            name='advisory',
        ),
        migrations.DeleteModel(
            name='Advisory',
        ),
        migrations.AlterField(
            model_name='referral',
            name='scholar',
            field=models.ForeignKey(to='students.Scholar'),
        ),
        migrations.DeleteModel(
            name='Scholar',
        ),
    ]
