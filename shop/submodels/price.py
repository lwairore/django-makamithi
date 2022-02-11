from django.db.models import (Model, ForeignKey, DecimalField, PROTECT)
from django.db.models.fields import DateTimeField


class PriceModel(Model):
    was = DecimalField(max_digits=10,
                       decimal_places=2,
                       blank=True,
                       null=True)

    now = DecimalField(max_digits=10,
                       decimal_places=2,
                       blank=True,
                       null=True)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return f'is {self.now}'

    class Meta:
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'
