from product.submodels.rating_scale import ProductReviewModel
from django.contrib.admin import ModelAdmin, register


@register(ProductReviewModel)
class ProductReviewModelAdmin(ModelAdmin):
    list_display = ('rating',)
