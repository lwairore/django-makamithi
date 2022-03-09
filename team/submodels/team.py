from home_two.models import PhotoModel
from django.core.exceptions import ValidationError
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, TextField, URLField
from django.db.models.fields.related import OneToOneField


class TeamModel(Model):
    image = OneToOneField(
        PhotoModel, blank=True, null=True, on_delete=PROTECT)
    full_name = CharField(max_length=70)
    role = CharField(max_length=70)
    facebook = URLField(blank=True, null=True)
    twitter = URLField(blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'
