from home_two.models import PhotoModel
from django.db.models import (
    Model, ForeignKey, CharField, PROTECT, ManyToManyField)
from django.db.models.fields import DateTimeField


class ProductModel(Model):
    title = CharField(max_length=250)
    category = ManyToManyField('ProductCategoryModel',
                               blank=True)
    price = ForeignKey('PriceModel', blank=True,null=True, on_delete=PROTECT)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)
    photo = ForeignKey(PhotoModel, blank=True, null=True, on_delete=PROTECT)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
