from django.db.models.base import Model
from django.db.models.deletion import PROTECT
from django.db.models.fields import CharField, DateTimeField, TextField
from django.db.models.fields.related import ForeignKey


class VisitNowCtaSectionModel(Model):
    heading = CharField(max_length=60)
    description = TextField(max_length=255, blank=True, null=True)
    background_image = ForeignKey(
        'PhotoModel', blank=True, null=True, on_delete=PROTECT,
        related_name='visit_now_cta_section_background_image')
    section_image = ForeignKey(
        'PhotoModel', blank=True, null=True, on_delete=PROTECT,
        related_name='visit_now_cta_section_section_image')
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.heading

    class Meta:
        verbose_name = 'Visit now cta section'
        verbose_name_plural = 'Visit now cta sections'
