from home_two.submodels.our_feature_section import FeatureSectionModel
from django.contrib.admin import ModelAdmin, register


@register(FeatureSectionModel)
class FeatureSectionModelAdmin(ModelAdmin):
    list_display = ('summary', 'background_image', 'section_image',)
    search_fields = ('summary',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at', 'modified_date',)
    raw_id_fields = ('background_image', 'section_image',)

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and FeatureSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
