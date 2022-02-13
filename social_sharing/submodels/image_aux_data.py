from home_two.submodels.preview_item import PhotoModel
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, PositiveIntegerField, TextField, URLField
from django.db.models.fields.related import ForeignKey


class ImageAuxDataModel(Model):
    width = PositiveIntegerField(blank=True, null=True)
    height = PositiveIntegerField(blank=True, null=True)
    image = ForeignKey(
        PhotoModel, blank=True, null=True, on_delete=PROTECT)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return f'Image ID={self.id}'

    class Meta:
        verbose_name = 'Image Auxilliary data'
        verbose_name_plural = 'Image auxilliary data'
