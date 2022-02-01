from product.submodels.category import ProductCategoryModel
from django.contrib.admin import ModelAdmin, register


@register(ProductCategoryModel)
class ProductCategoryModelAdmin(ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description',)
