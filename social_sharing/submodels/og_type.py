from social_sharing.og_type_values import OG_TYPE_VALUES
from django.db.models import Model
from django.db.models.fields import CharField, DateTimeField, TextField


class OgTypeModel(Model):
    type_option = CharField(max_length=30,
                            choices=OG_TYPE_VALUES)
    type_value = TextField(max_length=500, blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.type_option

    class Meta:
        verbose_name = 'Og type'
        verbose_name_plural = 'Og types'
