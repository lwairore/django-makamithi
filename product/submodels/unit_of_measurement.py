from django.db.models import (Model, CharField, TextField)
from django.db.models.fields import DateTimeField


class UnitOfMeasurementModel(Model):
    title = CharField(max_length=60)
    description = TextField(max_length=5000, blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Unit of measurement'
        verbose_name_plural = 'Units of measurement'
