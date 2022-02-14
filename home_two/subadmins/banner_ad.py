from home_two.submodels.banner_ad import BannerAdModel
from django.contrib.admin import ModelAdmin, register


@register(BannerAdModel)
class BannerAdModelAdmin(ModelAdmin):
    list_display = ('title', 'photo',)
    raw_id_fields = ('photo',)

    def has_delete_permission(self, request, obj=None):
        return False