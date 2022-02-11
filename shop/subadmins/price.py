from shop.submodels.price import PriceModel
from django.contrib.admin import ModelAdmin, register


@register(PriceModel)
class PriceModelAdmin(ModelAdmin):
    list_display = ('now', 'was',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at', 'modified_date',)
