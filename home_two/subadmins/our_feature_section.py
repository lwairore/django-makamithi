from home_two.submodels.our_feature_section import FeatureSectionModel
from django.contrib.admin import ModelAdmin, register


@register(FeatureSectionModel)
class FeatureSectionModelAdmin(ModelAdmin):
    list_display = ('summary', 'background_image', 'section_image',)
    search_fields = ('summary',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at', 'modified_date',)
    raw_id_fields = ('background_image',)
