from django.db import models

# Create your models here.

GRADE_CHOICES = (
    (1, '5'),
    (2, '6'),
    (3, '7'),
    (4, '8'),
)


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
    kbid = models.IntegerField(unique=True, primary_key=True)
    advisory = models.ForeignKey(Advisory)


