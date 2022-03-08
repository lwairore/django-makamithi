from django.core.exceptions import ValidationError
from home_two.submodels.preview_item import PhotoModel
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import DateTimeField
from django.db.models.fields.related import ForeignKey


class GalleryDetailSectionModel(Model):
    background_image = ForeignKey(
        PhotoModel, blank=True, null=True, on_delete=PROTECT)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return f'Gallery detail section'

    def clean(self):
        if GalleryDetailSectionModel.objects.exists() and not self.pk:
            raise ValidationError("You can only have one company")

    def save(self, *args, **kwargs):
        if not self.pk and GalleryDetailSectionModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There can be only one "GalleryDetailSectionModel" instance')
        return super(GalleryDetailSectionModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Gallery detail section'
        verbose_name_plural = 'Gallery detail section'
