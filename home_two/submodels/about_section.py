from django.db.models import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, TextField
from django.db.models.fields.related import ForeignKey


class AboutSectionModel(Model):
    heading = CharField(max_length=70)
    description = TextField(max_length=250, blank=True, null=True)
    photo = ForeignKey('PhotoModel', blank=True, null=True, on_delete=PROTECT)

    def __str__(self) -> str:
        return self.heading

    class Meta:
        verbose_name = 'About section'
        verbose_name_plural = 'About sections'
