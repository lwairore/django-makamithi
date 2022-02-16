from service.submodels.service import ServiceModel
from django.contrib.admin import ModelAdmin, register


@register(ServiceModel)
class ServiceModelAdmin(ModelAdmin):
    list_display = ('title', 'home_photo', 'about_photo',)
    search_fields = ('title', 'summary',)
    raw_id_fields = ('home_photo', 'about_photo',)
    date_hierarchy = 'modified_date'
    list_filter = ('created_at', 'modified_date',)
