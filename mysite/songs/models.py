from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_mysql.models import ListCharField


def validate_date(date_time):
    if date_time < timezone.now():
        raise ValidationError("Date cannot be in the past")


class Song(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    duration = models.PositiveIntegerField(
        null=False,
        blank=False,
        help_text=_('In Seconds'),
    )
    uploaded_time = models.DateTimeField(
        null=True,
        blank=True,
        default=None,
        validators=[validate_date]
    )


class Podcast(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    duration = models.PositiveIntegerField(
        null=False,
        blank=False,
        help_text=_('In Seconds'),
    )
    uploaded_time = models.DateTimeField(
        null=True,
        blank=True,
        default=None,
        validators=[validate_date]
    )
    host = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    participants = ListCharField(
        base_field=models.CharField(max_length=100),
        size=10,
        max_length=(10 * 101)
    )


class Audiobook(models.Model):
    title = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    author = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    narrator = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    duration = models.PositiveIntegerField(
        null=False,
        blank=False,
        help_text=_('In Seconds'),
    )
    uploaded_time = models.DateTimeField(
        null=True,
        blank=True,
        default=None,
        validators=[validate_date]
    )
