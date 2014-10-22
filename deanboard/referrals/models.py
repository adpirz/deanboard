from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

LEVEL_CHOICES = (
    (1, 'Teacher'),
    (2, 'Admin'),
    (3, 'Network Admin')
)

PREFIX_CHOICES = (
    (1, 'Mr.'),
    (2, 'Ms.'),
    (3, 'Mrs.'),
)

GRADE_CHOICES = (
    (1, '5'),
    (2, '6'),
    (3, '7'),
    (4, '8'),
)

REASONS_CHOICES = (
    (1, 'Repeated Infractions'),
    (2, 'Walked Out'),
    (3, 'Walked Away/Ignored'),
    (4, 'Abusive/Profane Language'),
    (5, 'Threatening/Bullying'),
    (6, 'Harassment (sexual, racial, etc.)'),
    (7, 'Preventing continuation of class'),
    (8, 'Inappropriate response to a consequence'),
    (9, 'Horseplay'),
    (10, 'Fight'),
)


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    level = models.IntegerField(choices=LEVEL_CHOICES, default=1)
    prefix = models.IntegerField(choices=PREFIX_CHOICES)

    def __unicode__(self):
        return self.user.username


class Advisory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    grade = models.IntegerField(choices=GRADE_CHOICES)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "advisories"


class Scholar(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    kbid = models.IntegerField(unique=True)
    advisory = models.ForeignKey(Advisory)

    def __unicode__(self):
        return self.last_name


class Referral(models.Model):
    uuid = models.CharField(max_length=200, default=lambda: uuid.uuid4().hex_digits())
    scholar = models.ForeignKey(Scholar)
    staff = models.ForeignKey(UserProfile)
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    reason = models.IntegerField(choices=REASONS_CHOICES)
    description = models.CharField(max_length=1000, default="")

    def __unicode__(self):
        return self.id
