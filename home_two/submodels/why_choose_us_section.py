from django.db.models.base import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import ForeignKey


class WhyChooseUsSectionModel(Model):
    heading = CharField(max_length=60)
    description = TextField(max_length=255, blank=True, null=True)
    section_image = ForeignKey(
        'PhotoModel', blank=True, null=True, on_delete=PROTECT,
        related_name='why_choose_us_section_section_image')
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.heading

    class Meta:
        verbose_name = 'Why choose us section'
        verbose_name_plural = 'Why choose us sections'
