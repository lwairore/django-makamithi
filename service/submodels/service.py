from home_two.submodels.preview_item import PhotoModel
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import ForeignKey


class ServiceModel(Model):
    photo = ForeignKey(PhotoModel, blank=True, null=True, on_delete=PROTECT)
    title = CharField(max_length=80)
    summary = TextField(max_length=120, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'