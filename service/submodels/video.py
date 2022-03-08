from django.core.exceptions import ValidationError
from django.db.models.deletion import PROTECT
from home_two.submodels.preview_item import PhotoModel
from django.db.models.fields.files import FileField, ImageField
from django.db.models.fields.related import ForeignKey
from custom_utils.rename_image_filename_util import rename_uploaded_image_and_path
from django.db.models import Model
from django.db.models.fields import CharField, DateTimeField, TextField


class VideoModel(Model):
    title = CharField(max_length=80)
    thumbnail = ForeignKey(
        PhotoModel, blank=True, null=True, on_delete=PROTECT)
    video = FileField(upload_to=rename_uploaded_image_and_path,
                      max_length=2000)
    caption = TextField(max_length=5000, blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return f'Image ID={self.title}'

    def clean(self):
        if VideoModel.objects.exists() and not self.pk:
            raise ValidationError("You can only have one company")

    def save(self, *args, **kwargs):
        if not self.pk and VideoModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There can be only one "VideoModel" instance')
        return super(VideoModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Video area section'
        verbose_name_plural = 'Video area section'

    class Meta:
        verbose_name = 'Video'
        verbose_name_plural = 'Videos'
