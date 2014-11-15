from django.db import models
from django.contrib.auth.models import User
import uuid
from students.models import Scholar, Advisory

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


class Referral(models.Model):
    scholar = models.ForeignKey(Scholar)
    staff = models.ForeignKey(UserProfile)
    datetime = models.DateTimeField(auto_now=True)
    reason = models.IntegerField(choices=REASONS_CHOICES)
    description = models.CharField(max_length=1000, default="")

    def __unicode__(self):
        return self.id
