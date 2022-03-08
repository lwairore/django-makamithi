from django.db.models.base import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import ForeignKey
from django.core.exceptions import ValidationError


class WhyChooseUsSectionModel(Model):
    heading = CharField(max_length=60)
    description = TextField(max_length=255, blank=True, null=True)
    section_image = ForeignKey(
        'PhotoModel', blank=True, null=True, on_delete=PROTECT,
        related_name='why_choose_us_section_section_image')
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.heading

    def clean(self):
        if WhyChooseUsSectionModel.objects.exists() and not self.pk:
            raise ValidationError("You can only have one company")

    def save(self, *args, **kwargs):
        if not self.pk and WhyChooseUsSectionModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There can be only one "WhyChooseUsSectionModel" instance')
        return super(WhyChooseUsSectionModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Why choose us section'
        verbose_name_plural = 'Why choose us section'
