from shop.submodels.product_category import ProductCategoryModel
from django.contrib.admin import ModelAdmin, register


@register(ProductCategoryModel)
class ProductCategoryModelAdmin(ModelAdmin):
    list_display = ('title', 'flaticon',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at', 'modified_date',)
    search_fields = ('title', 'description',)
