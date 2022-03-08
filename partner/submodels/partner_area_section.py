from django.core.exceptions import ValidationError
from django.db.models.fields import DateTimeField
from home_two.submodels import PhotoModel
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields.related import OneToOneField


class PartnerAreaSectionModel(Model):
    background_image = OneToOneField(
        PhotoModel, on_delete=PROTECT)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return 'Partner area section'

    def clean(self):
        if PartnerAreaSectionModel.objects.exists() and not self.pk:
            raise ValidationError("You can only have one company")

    def save(self, *args, **kwargs):
        if not self.pk and PartnerAreaSectionModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There can be only one "PartnerAreaSectionModel" instance')
        return super(PartnerAreaSectionModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Partner area section'
        verbose_name_plural = 'Partner area section'
