from social_sharing.submodels.seo_social_share_data import SeoSocialShareDataModel
from django.contrib.admin import ModelAdmin, register


@register(SeoSocialShareDataModel)
class SeoSocialShareDataModelAdmin(ModelAdmin):
    list_display = ('title', 'keywords', 'url', 'type',
                    'author', 'section', 'published', 'modified',)
    search_fields = ('title', 'keywords', 'description',
                     'url', 'type', 'author', 'section')
    raw_id_fields = ('image',)
    list_filter = ('modified_date', 'created_at',)
