from partner.models import PartnerModel
from django.contrib.admin import ModelAdmin, register
from django.utils.safestring import mark_safe


@register(PartnerModel)
class PartnerModelAdmin(ModelAdmin):
    list_display = ('title', 'link', 'image', 'modified_date',
                    'created_at', )
    date_hierarchy = 'created_at'
    raw_id_fields = ('image',)
    list_filter = ('modified_date', 'created_at',)
    readonly_fields = ('modified_date', 'created_at',
                       'image_preview',)
    search_fields = ('title', 'link',)
    fieldsets = (
        (None, {
            'fields': ('title', 'link',),
        }),
        ('Image', {
            'fields': ('image', 'image_preview',
                       ),
        }),
        (None, {
            'fields': ('created_at', 'modified_date',),
        }),
    )

    def image_preview(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.image.image.url,
        ))
