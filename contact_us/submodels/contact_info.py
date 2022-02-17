from django.core.exceptions import ValidationError
from django.db.models.fields import CharField, DateTimeField, EmailField, TextField
from home_two.submodels import PhotoModel
from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields.related import ForeignKey


class ContactInfoModel(Model):
    address_title = CharField(max_length=70)
    address_image = ForeignKey(
        PhotoModel, blank=True, null=True, on_delete=PROTECT)
    address = CharField(max_length=150)
    email = EmailField()
    phone_number = CharField(max_length=15)

    def __str__(self) -> str:
        return self.address_title

    class Meta:
        verbose_name = 'Contact info'
        verbose_name_plural = 'Contact infos'
