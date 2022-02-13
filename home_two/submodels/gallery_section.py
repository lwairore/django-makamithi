from django.core.exceptions import ValidationError
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import ForeignKey


class GallerySectionModel(Model):
    heading = CharField(max_length=60)
    summary = TextField(max_length=255, blank=True, null=True)
    section_image = ForeignKey(
        'PhotoModel', blank=True, null=True, on_delete=PROTECT, )
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.heading

    def clean(self):
        if GallerySectionModel.objects.exists() and not self.pk:
            raise ValidationError("You can only have one company")

    def save(self, *args, **kwargs):
        if not self.pk and GallerySectionModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There is can be only one "GallerySectionModel" instance')
        return super(GallerySectionModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Gallery section'
        verbose_name_plural = 'Gallery sections'
