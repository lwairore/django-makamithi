from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import OneToOneField


class CoreValueModel(Model):
    title = CharField(max_length=90)
    description = TextField(max_length=255, blank=True, null=True)
    image = OneToOneField(
        'PhotoModel', blank=True, null=True, on_delete=PROTECT)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Core value'
        verbose_name_plural = 'Core values'
