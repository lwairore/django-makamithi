from about_us.models import ClientReviewModel
from django.contrib.admin import ModelAdmin, register


@register(ClientReviewModel)
class ClientReviewModelAdmin(ModelAdmin):
    list_display = ('full_name', 'position', 'image', 'modified_date',
                    'created_at', )
    search_fields = ('full_name', 'image', 'review', 'position',)
    raw_id_fields = ('image',)
    date_hierarchy = 'created_at'
    list_filter = ('modified_date', 'created_at',)
