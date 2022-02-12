from shop.submodels.product import ProductModel
from django.contrib.admin import ModelAdmin, register


@register(ProductModel)
class ProductModelAdmin(ModelAdmin):
    list_display = ('title', 'photo',)
    raw_id_fields = ('photo', 'price', )
    filter_horizontal = ('category', )
    list_filter = ('created_at', 'modified_date',)
    date_hierarchy = 'created_at'
