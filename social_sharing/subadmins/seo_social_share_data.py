from django.contrib.admin import ModelAdmin


class SeoSocialShareDataModelAdmin(ModelAdmin):
    list_display = ('title', 'keywords', 'url', 'type',
                    'author', 'section', 'published', 'modified',)
    search_fields = ('title', 'keywords', 'description',
                     'url', 'type', 'author', 'section')
    raw_id_fields = ('image',)
    date_hierarchy = 'published'
    list_filter = ('modified', 'published',)
