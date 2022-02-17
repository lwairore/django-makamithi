from contact_us.models import ContactInfoModel
from django.contrib.admin import ModelAdmin, register


@register(ContactInfoModel)
class ContactInfoModelAdmin(ModelAdmin):
    list_display = ('address_title', 'address_image',
                    'address', 'email', 'phone_number',)
    list_filter = ('modified_date', 'created_at',)
    raw_id_fields = ('address_image',)
    date_hierarchy = 'created_at'
    search_fields = ('address_title', 'address_image',
                     'address', 'email', 'phone_number',)
