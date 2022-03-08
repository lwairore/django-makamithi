from contact_us.models import WorkWithUsCtaSectionModel
from django.contrib.admin import ModelAdmin, register


@register(WorkWithUsCtaSectionModel)
class WorkWithUsCtaSectionModelAdmin(ModelAdmin):
    list_display = ('heading', 'call_to_action', 'background_image',
                    'section_image', 'modified_date', 'created_at',)
    date_hierarchy = 'created_at'
    raw_id_fields = ('background_image', 'section_image',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and WorkWithUsCtaSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
