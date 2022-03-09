from home_two.submodels.preview_item import PhotoModel
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import (
    OneToOneField, ManyToManyField, OneToOneField)


class ServiceModel(Model):
    title = CharField(max_length=80)
    keywords = CharField(max_length=180, blank=True, null=True)
    summary = TextField(max_length=120, blank=True, null=True)
    description = TextField(max_length=1200, blank=True, null=True)
    home_photo = OneToOneField(PhotoModel, blank=True,
                               null=True, on_delete=PROTECT, related_name='service_model_home_photo')
    about_photo = OneToOneField(PhotoModel, blank=True,
                                null=True, on_delete=PROTECT, related_name='service_model_about_photo')
    service_page_photo = OneToOneField(PhotoModel, blank=True,
                                       null=True, on_delete=PROTECT, related_name='service_model_service_page_photo')
    service_detail_photo = OneToOneField(PhotoModel, blank=True,
                                         null=True, on_delete=PROTECT, related_name='service_model_service_detail_photo')
    nav_sidebar_photo = OneToOneField(PhotoModel, blank=True,
                                      null=True, on_delete=PROTECT, related_name='service_model_sidebar_photo')
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)
    plans = ManyToManyField('PlanModel', blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
