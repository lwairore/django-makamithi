from home_two.submodels.visit_now_cta_section import VisitNowCtaSectionModel
from django.contrib.admin import ModelAdmin, register


@register(VisitNowCtaSectionModel)
class VisitNowCtaSectionModelAdmin(ModelAdmin):
    list_display = ('heading', 'background_image',
                    'section_image', 'modified_date', 'created_at',)
    list_filter = ('modified_date', 'created_at',)
    search_fields = ('heading', 'description',)
    date_hierarchy = 'created_at'
    raw_id_fields = ('background_image', 'section_image',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and VisitNowCtaSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
