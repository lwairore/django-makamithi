from gallery.submodels import GalleryModel
from django.contrib.admin import ModelAdmin, register


@register(GalleryModel)
class GalleryModelAdmin(ModelAdmin):
    list_display = ('id', 'image',)
    date_hierarchy = 'created_at'
    raw_id_fields = ('image',)
    list_filter = ('modified_date', 'created_at',)
