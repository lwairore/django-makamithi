from django.contrib.admin import ModelAdmin


class SeoSocialShareDataModelAdmin(ModelAdmin):
    list_display = ('title', 'keywords', 'type',
                    'author', 'section', 'published', 'modified',)
    raw_id_fields = ('image',)
    date_hierarchy = 'published'
