from product.submodels.product import ProductModel
from django.contrib.admin import ModelAdmin, register


@register(ProductModel)
class ProductModelAdmin(ModelAdmin):
    list_display = ('title', 'category',)
    raw_id_fields = ('category',)
    fieldsets = (
        (None, {
            'fields': ('title',)
        },),
        ('Product category', {
            'fields': ('category',)
        },),
    )
