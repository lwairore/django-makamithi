from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import ForeignKey


class FeatureSectionModel(Model):
    description = TextField(max_length=250, blank=True, null=True)
    photo = ForeignKey('PhotoModel', blank=True, null=True, on_delete=PROTECT)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.description

    class Meta:
        verbose_name = 'Feature section'
        verbose_name_plural = 'Feature sections'
