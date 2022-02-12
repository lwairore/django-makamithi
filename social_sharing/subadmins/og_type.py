from django.contrib.admin.decorators import register
from social_sharing.submodels.og_type import OgTypeModel
from django.contrib.admin import ModelAdmin, regist


@register(OgTypeModel)
class OgTypeModelAdmin(ModelAdmin):
    list_display = ('type_option', 'modified_date', 'created_at',)
    date_hierarchy = 'created_at'
    search_fields = ('type_option', 'type_value',)
    list_filter = ('modified_date', 'created_at',)
