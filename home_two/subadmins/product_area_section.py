from home_two.models import ProductAreaSectionModel
from django.contrib.admin import ModelAdmin, register


@register(ProductAreaSectionModel)
class ProductAreaSectionModelAdmin(ModelAdmin):
    list_display = ('heading', 'section_image', 'created_at', 'modified_date',)
    date_hierarchy = 'created_at'
    raw_id_fields = ('section_image',)

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and ProductAreaSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance

    def has_delete_permission(self, request, obj=None):
        return False
