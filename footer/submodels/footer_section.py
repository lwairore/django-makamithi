from django.core.exceptions import ValidationError
from home_two.submodels.preview_item import PhotoModel
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import DateTimeField, TextField
from django.db.models.fields.related import OneToOneField


class FooterSectionModel(Model):
    footer_text = TextField(max_length=250)
    section_image = OneToOneField(
        PhotoModel, on_delete=PROTECT, related_name='footer_section_section_image',
        blank=True, null=True)
    background_image = OneToOneField(
        PhotoModel, on_delete=PROTECT, related_name='footer_section_background_image',
        blank=True, null=True)
    footer_logo = OneToOneField(
        PhotoModel, on_delete=PROTECT,
        related_name='footer_section_footer_logo')
    created_at = DateTimeField(auto_now_add=True)
    modified_date = DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.footer_text[:60]

    def clean(self):
        if FooterSectionModel.objects.exists() and not self.pk:
            raise ValidationError("You can only have one company")

    def save(self, *args, **kwargs):
        if not self.pk and FooterSectionModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There can be only one "FooterSectionModel" instance')
        return super(FooterSectionModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Footer section'
        verbose_name_plural = 'Footer section'
