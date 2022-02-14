from home_two.submodels.preview_item import PhotoModel
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, PositiveIntegerField, TextField, URLField
from django.db.models.fields.related import ForeignKey


class SeoSocialShareDataModel(Model):
    title = CharField(max_length=80)
    keywords = CharField(max_length=80, blank=True, null=True)
    description = TextField(max_length=466, blank=True, null=True)
    image = ForeignKey(
        PhotoModel, blank=True, null=True, on_delete=PROTECT)
    type = CharField(max_length=80, blank=True, null=True)
    author = CharField(max_length=160, blank=True, null=True)
    section = CharField(max_length=160, blank=True, null=True)
    published = DateTimeField(auto_now=True, blank=True, null=True)
    modified = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        abstract = True
        verbose_name = 'SEO social sharing detail'
        verbose_name_plural = 'SEO social sharing details'
