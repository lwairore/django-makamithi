from django.db.models import (
    Model, ForeignKey, CharField, PROTECT, ManyToManyField)


class ProductModel(Model):
    title = CharField(max_length=250)
    category = ForeignKey('ProductCategoryModel', on_delete=PROTECT,
                          blank=True, null=True, related_name='product_category')
    price = ManyToManyField('PriceModel', blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
