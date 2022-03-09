from django.db.models.base import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import OneToOneField
from django.core.exceptions import ValidationError


class CounterAreaSectionModel(Model):
    heading = CharField(max_length=80)
    background_image = OneToOneField(
        'PhotoModel', blank=True, null=True, on_delete=PROTECT)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.heading

    def clean(self):
        if CounterAreaSectionModel.objects.exists() and not self.pk:
            raise ValidationError("You can only have one company")

    def save(self, *args, **kwargs):
        if not self.pk and CounterAreaSectionModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There can be only one "CounterAreaSectionModel" instance')
        return super(CounterAreaSectionModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Counter area section'
        verbose_name_plural = 'Counter area section'
