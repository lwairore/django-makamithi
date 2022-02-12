from social_sharing.submodels.image_aux_data import ImageAuxDataModel
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, PositiveIntegerField, TextField, URLField
from django.db.models.fields.related import ForeignKey


class SeoSocialShareDataModel(Model):
    title = CharField(max_length=70)
    keywords = CharField(max_length=80, blank=True, null=True)
    description = TextField(max_length=180, blank=True, null=True)
    image = ForeignKey(
        ImageAuxDataModel, blank=True, null=True, on_delete=PROTECT)
    url = URLField(blank=True, null=True)
    type = ForeignKey('OgTypeModel', blank=True, null=True, on_delete=PROTECT)
