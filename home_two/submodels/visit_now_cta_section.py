from django.core.exceptions import ValidationError
from django.db.models.base import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import ForeignKey


class VisitNowCtaSectionModel(Model):
    heading = CharField(max_length=60)
    description = TextField(max_length=255, blank=True, null=True)
    background_image = ForeignKey(
        'PhotoModel', blank=True, null=True, on_delete=PROTECT,
        related_name='visit_now_cta_section_background_image')
    section_image = ForeignKey(
        'PhotoModel', blank=True, null=True, on_delete=PROTECT,
        related_name='visit_now_cta_section_section_image')
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.heading

    def __str__(self) -> str:
        return self.heading

    def clean(self):
        if VisitNowCtaSectionModel.objects.exists() and not self.pk:
            raise ValidationError("You can only have one company")

    def save(self, *args, **kwargs):
        if not self.pk and VisitNowCtaSectionModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There can be only one "VisitNowCtaSectionModel" instance')
        return super(VisitNowCtaSectionModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Visit now cta section'
        verbose_name_plural = 'Visit now cta section'
