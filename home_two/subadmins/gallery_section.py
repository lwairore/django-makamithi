from home_two.submodels import GallerySectionModel
from django.contrib.admin import ModelAdmin, register


@register(GallerySectionModel)
class GallerySectionModelAdmin(ModelAdmin):
    date_hierarchy = 'created_at'
    raw_id_fields = ('section_image', 'background_image',)
    list_display = ('heading', 'summary', 'section_image', 'background_image',
                    'modified_date', 'created_at',)

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and GallerySectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance

    def has_delete_permission(self, request, obj=None):
        return False
