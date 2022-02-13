from django.db.models.fields import DateTimeField
from home_two.submodels import PhotoModel
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields.related import ForeignKey


class GalleryModel(Model):
    image = ForeignKey(
        PhotoModel, blank=True, null=True, on_delete=PROTECT)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return f'Gallery ID={self.id}'

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'
