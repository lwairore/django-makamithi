from inbox.submodels.inbox import InboxModel
from django.contrib.admin import ModelAdmin, register


@register(InboxModel)
class InboxModelAdmin(ModelAdmin):
    list_display = ('name', 'subject', 'read', 'email',
                    'phone_number', 'created_at', 'modified_date')
    search_fields = ('name', 'subject', 'email', 'phone_number', 'message',)
    date_hierarchy = 'created_at'
    list_editable = ('read',)
    list_filter = ('read', 'created_at', 'modified_date',)
