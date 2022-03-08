from django.db.models.base import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import (
    PositiveIntegerField, DateTimeField, CharField)
from django.db.models.fields.related import ForeignKey
from django.core.exceptions import ValidationError


class BadgeModel(Model):
    number_of_years = PositiveIntegerField()
    title = CharField(max_length=70, blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Badge'
        verbose_name_plural = 'Badges'
