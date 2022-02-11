from shop.submodels.product import ProductModel
from django.contrib.admin import ModelAdmin, register


@register(ProductModel)
class ProductModelAdmin(ModelAdmin):
    list_display = ('title', 'category', 'photo',)
    raw_id_fields = ('category', 'photo',)
    filter_horizontal = ('price',)
    list_filter = ('created_at', 'modified_date',)
    date_hierarchy = 'created_at'
