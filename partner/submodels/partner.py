from home_two.submodels.preview_item import PhotoModel
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, URLField
from django.db.models.fields.related import OneToOneField


class PartnerModel(Model):
    title = CharField(max_length=150)
    link = URLField()
    image = OneToOneField(to=PhotoModel, on_delete=PROTECT)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Partner'
        verbose_name_plural = 'Partners'
