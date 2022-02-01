from django.db.models import (Model, CharField, DecimalField)


class PriceModel(Model):
    was = DecimalField(max_digits=10,
                       decimal_places=2,
                       blank=True,
                       null=True)

    now = DecimalField(max_digits=10,
                       decimal_places=2,
                       blank=True,
                       null=True)
    per = CharField(max_length=60, blank=True, null=True)

    def __str__(self) -> str:
        return 'is {}'.format(self.now)

    class Meta:
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'
