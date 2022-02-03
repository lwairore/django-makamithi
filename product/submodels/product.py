from django.db.models import (
    Model, ForeignKey, CharField, PROTECT, ManyToManyField)
from django.db.models.fields import DateTimeField


class ProductModel(Model):
    title = CharField(max_length=250)
    category = ForeignKey('ProductCategoryModel', on_delete=PROTECT,
                          blank=True, null=True, related_name='product_category')
    price = ManyToManyField('PriceModel', blank=True)
    reviews = ManyToManyField('ProductReviewModel', blank=True)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
