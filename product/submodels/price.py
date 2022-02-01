from django.db.models import (Model, DecimalField)


class PriceModel(Model):
    was = DecimalField(max_digits=10,
                       decimal_places=2,
                       blank=True,
                       null=True)

    now = DecimalField(max_digits=10,
                       decimal_places=2,
                       blank=True,
                       null=True)
