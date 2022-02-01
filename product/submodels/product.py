from django.db.models import Model, ForeignKey, CharField, PROTECT


class ProductModel(Model):
    title = CharField(max_length=80)
    category = ForeignKey('ProductCategoryModel', on_delete=PROTECT,
                          blank=True, null=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
