from home_two.models import PhotoModel
from django.core.exceptions import ValidationError
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, TextField, URLField
from django.db.models.fields.related import ForeignKey


class TeamModel(Model):
    image = ForeignKey(
        PhotoModel, blank=True, null=True, on_delete=PROTECT)
    full_name = CharField(max_length=70)
    role = CharField(max_length=70)
    facebook = URLField(blank=True, null=True)
    twitter = URLField(blank=True, null=True)

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
