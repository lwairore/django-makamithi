from home_two.submodels.preview_item import PhotoModel
from django.core.exceptions import ValidationError
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import ForeignKey


class ClientReviewModel(Model):
    full_name = CharField(max_length=150)
    review = TextField(max_length=500)
    image = ForeignKey(
        PhotoModel, blank=True, null=True, on_delete=PROTECT)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.full_name

    class Meta:
        verbose_name = 'Client review'
        verbose_name_plural = 'Client reviews'
