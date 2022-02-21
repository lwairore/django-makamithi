from service.models import ServiceAreaSectionModel
from django.contrib.admin import ModelAdmin, register


@register(ServiceAreaSectionModel)
class ServiceAreaSectionModelAdmin(ModelAdmin):
    list_display = ('heading', 'years_of_experience_image', 'modified_date',
                    'created_at', )
    date_hierarchy = 'created_at'
    raw_id_fields = ('years_of_experience_image',)
    search_fields = ('heading', 'description',)
    list_filter = ('modified_date', 'created_at',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and ServiceAreaSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
