from django.core.exceptions import ValidationError
from home_two.submodels.preview_item import PhotoModel
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, EmailField
from django.db.models.fields.related import OneToOneField


class HeaderSectionModel(Model):
    primary_location = CharField(max_length=80)
    primary_email = EmailField()
    whatsapp_business_number = CharField(max_length=15, blank=True, null=True)
    logo_side = OneToOneField(
        PhotoModel, on_delete=PROTECT,
        related_name='header_section_logo_side')
    standard_logo = OneToOneField(
        PhotoModel, on_delete=PROTECT,
        related_name='header_section_standard_logo')
    retina_logo = OneToOneField(
        PhotoModel, on_delete=PROTECT,
        related_name='header_section_retina_logo')
    created_at = DateTimeField(auto_now_add=True)
    modified_date = DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.primary_location

    def clean(self):
        if HeaderSectionModel.objects.exists() and not self.pk:
            raise ValidationError("You can only have one company")

    def save(self, *args, **kwargs):
        if not self.pk and HeaderSectionModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There can be only one "HeaderSectionModel" instance')
        return super(HeaderSectionModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Header section'
        verbose_name_plural = 'Header section'
