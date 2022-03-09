from django.core.exceptions import ValidationError
from django.db.models.fields import CharField, DateTimeField, TextField
from home_two.submodels import PhotoModel
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields.related import OneToOneField


class ServiceSidebarSectionModel(Model):
    heading = CharField(max_length=70)
    summary = TextField(max_length=500, blank=True, null=True)
    background_image = OneToOneField(
        PhotoModel, blank=True, null=True, on_delete=PROTECT,
        related_name='service_sidebar_section_background_image')
    section_image = OneToOneField(
        PhotoModel, blank=True, null=True, on_delete=PROTECT,
        related_name='service_sidebar_section_section_image')
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.heading

    def clean(self):
        if ServiceSidebarSectionModel.objects.exists() and not self.pk:
            raise ValidationError("You can only have one company")

    def save(self, *args, **kwargs):
        if not self.pk and ServiceSidebarSectionModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There can be only one "ServiceSidebarSectionModel" instance')
        return super(ServiceSidebarSectionModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Service sidebar section'
        verbose_name_plural = 'Service sidebar section'
