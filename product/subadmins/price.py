from product.submodels.price import PriceModel
from django.contrib.admin import ModelAdmin, register


@register(PriceModel)
class PriceModelAdmin(ModelAdmin):
    list_display = ('now', 'was', 'per',)
    raw_id_fields = ('per',)
    fieldsets = (
        (None, {
            'fields': ('now', 'was', 'per',)
        },),
    )
