from django.db.models import Model
from django.db.models.fields import CharField, TextField


class BannerAdModel(Model):
    title = CharField(max_length=70)
    description = TextField(max_length=140)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Banner ad'
        verbose_name_plural = 'Banner ads'
