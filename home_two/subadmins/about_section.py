from home_two.submodels.about_section import AboutSectionModel
from django.contrib.admin import ModelAdmin, register


@register(AboutSectionModel)
class AboutSectionModelAdmin(ModelAdmin):
    list_display = ('heading', 'subheading','photo',)
    raw_id_fields = ('photo',)
