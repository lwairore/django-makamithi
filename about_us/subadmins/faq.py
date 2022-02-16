from about_us.models import FaqModel
from django.contrib.admin import ModelAdmin, register


@register(FaqModel)
class FaqModelAdmin(ModelAdmin):
    list_display = ('question', 'modified_date',
                    'created_at', )
    date_hierarchy = 'created_at'
    list_filter = ('modified_date', 'created_at',)
    