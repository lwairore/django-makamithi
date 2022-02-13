from home_two.submodels import CoreValueModel
from django.contrib.admin import ModelAdmin, register


@register(CoreValueModel)
class CoreValueModelAdmin(ModelAdmin):
    list_display = ('title', 'image', 'created_at', 'modified_date')
    search_fields = ('title', 'description',)
    list_filter = ('created_at', 'modified_date',)
    date_hierarchy = 'created_at'
    raw_id_fields = ('image',)
