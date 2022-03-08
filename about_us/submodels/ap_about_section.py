from django.core.exceptions import ValidationError
from django.db.models.fields import CharField, DateTimeField, TextField
from home_two.submodels import PhotoModel
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields.related import ForeignKey


class ApAboutSectionModel(Model):
    heading = CharField(max_length=70)
    subheading = CharField(max_length=70)
    description = TextField(max_length=500, blank=True, null=True)
    section_image = ForeignKey(
        PhotoModel, blank=True, null=True, on_delete=PROTECT)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.heading

    def clean(self):
        if ApAboutSectionModel.objects.exists() and not self.pk:
            raise ValidationError("You can only have one company")

    def save(self, *args, **kwargs):
        if not self.pk and ApAboutSectionModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There can be only one "ApAboutSectionModel" instance')
        return super(ApAboutSectionModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Ap About section'
        verbose_name_plural = 'Ap About section'
