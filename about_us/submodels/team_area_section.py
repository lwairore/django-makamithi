from django.core.exceptions import ValidationError
from home_two.submodels.preview_item import PhotoModel
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import ForeignKey


class TeamAreaSectionModel(Model):
    heading = CharField(max_length=80)
    section_image = ForeignKey(
        PhotoModel, blank=True, null=True, on_delete=PROTECT)
    summary = TextField(max_length=250, blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.heading

    def clean(self):
        if TeamAreaSectionModel.objects.exists() and not self.pk:
            raise ValidationError("You can only have one company")

    def save(self, *args, **kwargs):
        if not self.pk and TeamAreaSectionModel.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model
            raise ValidationError(
                'There can be only one "TeamAreaSectionModel" instance')
        return super(TeamAreaSectionModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Team area section'
        verbose_name_plural = 'Team area section'
