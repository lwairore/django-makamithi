from service.submodels.service import ServiceModel
from django.contrib.admin import ModelAdmin, register


@register(ServiceModel)
class ServiceModelAdmin(ModelAdmin):
    list_display = ('title', 'photo',)
    raw_id_fields = ('photo',)
