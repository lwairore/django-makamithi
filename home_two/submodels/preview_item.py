from django.db.models.fields.files import ImageField
from custom_utils.rename_image_filename_util import rename_uploaded_image_and_path
from django.db.models import Model
from django.db.models.fields import DateTimeField, PositiveIntegerField, TextField


class PhotoModel(Model):
    width = PositiveIntegerField(blank=True, null=True)
    height = PositiveIntegerField(blank=True, null=True)
    image = ImageField(upload_to=rename_uploaded_image_and_path,
                       max_length=2000)
    caption = TextField(max_length=5000, blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return f'Image ID={self.id}'

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
