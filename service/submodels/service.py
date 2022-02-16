from home_two.submodels.preview_item import PhotoModel
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import ForeignKey


class ServiceModel(Model):
    home_photo = ForeignKey(PhotoModel, blank=True,
                            null=True, on_delete=PROTECT, related_name='service_model_home_photo')
    about_photo = ForeignKey(PhotoModel, blank=True,
                            null=True, on_delete=PROTECT, related_name='service_model_about_photo')
    title = CharField(max_length=80)
    summary = TextField(max_length=120, blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
