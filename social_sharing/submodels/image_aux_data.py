from home_two.submodels.preview_item import PhotoModel
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, PositiveIntegerField, TextField, URLField
from django.db.models.fields.related import ForeignKey


class ImageAuxDataModel(Model):
    width = PositiveIntegerField(blank=True, null=True)
    height = PositiveIntegerField(blank=True, null=True)
    secure_url = URLField(blank=True, null=True)
    mimeType = CharField(max_length=128, blank=True, null=True)
    alt = TextField(max_length=500, blank=True, null=True)
    image = ForeignKey(
        PhotoModel, blank=True, null=True, on_delete=PROTECT)

    def __str__(self) -> str:
        return f'Image ID={self.id}'

    class Meta:
        verbose_name = 'Image Auxilliary data'
        verbose_name_plural = 'Image auxilliary data'