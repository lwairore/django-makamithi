from partner.models import PartnerModel
from django.contrib.admin import ModelAdmin, register


@register(PartnerModel)
class PartnerModelAdmin(ModelAdmin):
    list_display = ('title', 'link', 'image', 'modified_date',
                    'created_at', )
    date_hierarchy = 'created_at'
    raw_id_fields = ('image',)
    list_filter = ('modified_date', 'created_at',)
    search_fields = ('title', 'link',)
