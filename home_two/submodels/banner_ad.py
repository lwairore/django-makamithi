from django.db.models import Model, PROTECT
from django.db.models.fields import (CharField, DateTimeField, TextField)
from django.db.models.fields.related import OneToOneField


class BannerAdModel(Model):
    title = CharField(max_length=70)
    description = TextField(max_length=250, blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)
    photo = OneToOneField('PhotoModel', blank=True,
                          null=True, on_delete=PROTECT)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Banner ad'
        verbose_name_plural = 'Banner ads'
