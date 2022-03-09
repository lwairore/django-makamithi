from django.core.exceptions import ValidationError
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import OneToOneField


class ProductAreaSectionModel(Model):
    heading = CharField(max_length=60)
    summary = TextField(max_length=250, blank=True, null=True)
    section_image = OneToOneField(
        'PhotoModel', blank=True, null=True, on_delete=PROTECT)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.summary

    def clean(self):
        if ProductAreaSectionModel.objects.exists() and not self.pk:
            raise ValidationError("You can only have one company")

    def save(self, *args, **kwargs):
        if not self.pk and ProductAreaSectionModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There can be only one "ProductAreaSectionModel" instance')
        return super(ProductAreaSectionModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Product area section'
        verbose_name_plural = 'Product area section'
