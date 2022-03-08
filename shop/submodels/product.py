from home_two.submodels.preview_item import PhotoModel
from django.db.models import (
    Model, ForeignKey, CharField, PROTECT, ManyToManyField)
from django.db.models.fields import DateTimeField, PositiveIntegerField, TextField


class ProductModel(Model):
    title = CharField(max_length=250)
    keywords = CharField(max_length=80, blank=True, null=True)
    category = ManyToManyField('ProductCategoryModel',
                               blank=True)
    total_sales = PositiveIntegerField(blank=True, null=True)
    price = ForeignKey('PriceModel', blank=True, null=True, on_delete=PROTECT)
    description = TextField(max_length=5000, blank=True, null=True)
    created_at = DateTimeField(auto_now_add=True, blank=True, null=True)
    modified_date = DateTimeField(auto_now=True, blank=True, null=True)
    product_preview = ForeignKey(PhotoModel, blank=True, null=True, on_delete=PROTECT,
                                 related_name='product_model_product_preview')
    product_images = ManyToManyField(
        PhotoModel, blank=True, related_name='product_model_product_images')
    reviews = ManyToManyField('ProductReview', blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
