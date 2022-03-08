from service.submodels.service import ServiceModel
from django.contrib.admin import ModelAdmin, register


@register(ServiceModel)
class ServiceModelAdmin(ModelAdmin):
    list_display = ('title', 'keywords', 'home_photo', 'about_photo', 'nav_sidebar_photo',
                    'service_page_photo', 'service_detail_photo', 'created_at', 'modified_date',)
    search_fields = ('title', 'summary', 'keywords',)
    raw_id_fields = ('home_photo', 'about_photo', 'nav_sidebar_photo',
                     'service_page_photo', 'service_detail_photo',)
    date_hierarchy = 'modified_date'
    list_filter = ('created_at', 'modified_date',)
    filter_horizontal = ('plans',)
