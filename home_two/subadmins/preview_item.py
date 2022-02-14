from home_two.models import PhotoModel
from django.contrib.admin import ModelAdmin, register


@register(PhotoModel)
class PhotoModelAdmin(ModelAdmin):
    list_display = ('id', 'image', 'width', 'height',)
    date_hierarchy = 'created_at'
    list_filter = ('modified_date', 'created_at')
    search_fields = ('caption', 'width', 'height',)
