from home.submodels.banner_ad import BannerAdModel
from django.contrib.admin import ModelAdmin, register
from django.utils.html import format_html


@register(BannerAdModel)
class BannerAdModelAdmin(ModelAdmin):
    list_display = ('title', 'number_of_photos',)
    filter_horizontal = ('photos',)

    def number_of_photos(self, obj: BannerAdModel):
        photos_count = obj.photos.all()\
            .order_by().only('id').count()

        return format_html("<b><i>{}</i></b>", photos_count)

    number_of_photos.short_description = 'Total photos'
