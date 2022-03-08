from home_two.submodels.preview_item import PhotoModel
from django.core.exceptions import ValidationError
from django.db.models.base import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import OneToOneField


class WorkWithUsCtaSectionModel(Model):
    heading = CharField(max_length=60)
    description = TextField(max_length=255, blank=True, null=True)
    call_to_action = CharField(max_length=70)
    background_image = OneToOneField(
        PhotoModel, on_delete=PROTECT,
        related_name='work_with_us_cta_section_background_image')
    section_image = OneToOneField(
        PhotoModel, on_delete=PROTECT,
        related_name='work_with_us_cta_section_section_image')
    created_at = DateTimeField(auto_now_add=True)
    modified_date = DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.heading

    def __str__(self) -> str:
        return self.heading

    def clean(self):
        if WorkWithUsCtaSectionModel.objects.exists() and not self.pk:
            raise ValidationError("You can only have one company")

    def save(self, *args, **kwargs):
        if not self.pk and WorkWithUsCtaSectionModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There can be only one "WorkWithUsCtaSectionModel" instance')
        return super(WorkWithUsCtaSectionModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Work with us cta section'
        verbose_name_plural = 'Work with us cta section'
