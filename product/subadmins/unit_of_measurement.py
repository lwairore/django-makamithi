from product.submodels.unit_of_measurement import UnitOfMeasurementModel
from django.contrib.admin import ModelAdmin, register


@register(UnitOfMeasurementModel)
class UnitOfMeasurementModelAdmin(ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description',)
