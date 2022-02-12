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
