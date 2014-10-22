# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advisory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128)),
                ('grade', models.IntegerField(choices=[(1, b'5'), (2, b'6'), (3, b'7'), (4, b'8')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Referral',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('reason', models.IntegerField(choices=[(1, b'Repeated Infractions'), (2, b'Walked Out'), (3, b'Walked Away/Ignored'), (4, b'Abusive/Profane Language'), (5, b'Threatening/Bullying'), (6, b'Harassment (sexual, racial, etc.)'), (7, b'Preventing continuation of class'), (8, b'Inappropriate response to a consequence'), (9, b'Horseplay'), (10, b'Fight')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scholar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('kbid', models.IntegerField(unique=True)),
                ('advisory', models.ForeignKey(to='referrals.Advisory')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.IntegerField(default=1, choices=[(1, b'Teacher'), (2, b'Admin')])),
                ('prefix', models.IntegerField(choices=[(1, b'Mr.'), (2, b'Ms.'), (3, b'Mrs.')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='referral',
            name='scholar',
            field=models.ForeignKey(to='referrals.Scholar'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='referral',
            name='staff',
            field=models.ForeignKey(to='referrals.UserProfile'),
            preserve_default=True,
        ),
    ]
