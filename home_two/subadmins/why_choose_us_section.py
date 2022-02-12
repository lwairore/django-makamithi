from home_two.submodels.why_choose_us_section import WhyChooseUsSectionModel
from django.contrib.admin import ModelAdmin, register


@register(WhyChooseUsSectionModel)
class WhyChooseUsSectionModelAdmin(ModelAdmin):
    list_display = ('heading', 'section_image', 'modified_date', 'created_at',)
    list_filter = ('modified_date', 'created_at',)
    search_fields = ('heading', 'description',)
    date_hierarchy = 'created_at'
    raw_id_fields = ('section_image',)
