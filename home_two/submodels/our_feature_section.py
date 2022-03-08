from django.core.exceptions import ValidationError
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import ForeignKey


class FeatureSectionModel(Model):
    summary = TextField(max_length=250, blank=True, null=True)
    background_image = ForeignKey(
        'PhotoModel', blank=True, null=True, on_delete=PROTECT,
        related_name='feature_section_background_image')
    section_image = ForeignKey(
        'PhotoModel', blank=True, null=True, on_delete=PROTECT,
        related_name='feature_section_section_image')
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.summary

    def clean(self):
        if FeatureSectionModel.objects.exists() and not self.pk:
            raise ValidationError("You can only have one company")

    def save(self, *args, **kwargs):
        if not self.pk and FeatureSectionModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There can be only one "FeatureSectionModel" instance')
        return super(FeatureSectionModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Feature section'
        verbose_name_plural = 'Feature section'
