from django.core.exceptions import ValidationError
from django.db.models.fields import DateTimeField
from home_two.submodels import PhotoModel
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields.related import OneToOneField


class SiteBreadcrumbModel(Model):
    background_image = OneToOneField(
        PhotoModel, blank=True, null=True, on_delete=PROTECT)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return f'Site breadcrumb ID={self.id}'

    def clean(self):
        if SiteBreadcrumbModel.objects.exists() and not self.pk:
            raise ValidationError("You can only have one company")

    def save(self, *args, **kwargs):
        if not self.pk and SiteBreadcrumbModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There can be only one "SiteBreadcrumbModel" instance')
        return super(SiteBreadcrumbModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Site breadcrumb'
        verbose_name_plural = 'Site breadcrumbs'
