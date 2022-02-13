from social_sharing.submodels.image_aux_data import ImageAuxDataModel
from django.contrib.admin import ModelAdmin, register


@register(ImageAuxDataModel)
class ImageAuxDataModelAdmin(ModelAdmin):
    list_display = ('width', 'height',
                    'image',)
    list_filter = ('modified_date', 'created_at',)
    search_fields = ('width', 'height',
                     'image',)
    date_hierarchy = 'created_at'
    raw_id_fields = ('image',)
