from partner.models import PartnerAreaSectionModel
from django.contrib.admin import ModelAdmin, register
from django.utils.safestring import mark_safe


@register(PartnerAreaSectionModel)
class PartnerAreaSectionModelAdmin(ModelAdmin):
    list_display = ('background_image', 'modified_date',
                    'created_at', )
    date_hierarchy = 'created_at'
    raw_id_fields = ('background_image',)
    readonly_fields = ('modified_date',
                       'created_at', 'background_image_preview',)
    fieldsets = (
        ('Preview', {
            'fields': (
                'background_image', 'background_image_preview',
            ),
        }),
        (None, {
            'fields': ('created_at', 'modified_date',),
        }),
    )

    def background_image_preview(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.background_image.image.url,
        ))

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and PartnerAreaSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
