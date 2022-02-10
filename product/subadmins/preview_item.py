from product.submodels.preview_item import PhotoModel
from product.submodels.banner_ad import BannerAdModel
from django.contrib.admin import ModelAdmin, register


@register(PhotoModel)
class PhotoModelAdmin(ModelAdmin):
    list_display = ('id', 'image',)
    date_hierarchy = 'created_at'
    list_filter = ('modified_date',)
