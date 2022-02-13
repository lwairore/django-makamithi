from django.contrib.admin import ModelAdmin


class SeoSocialShareDataModelAdmin(ModelAdmin):
    list_display = ('title', 'keywords', 'type',
                    'author', 'section', 'published', 'modified',)
    search_fields = ('title', 'keywords', 'description',
                     'type', 'author', 'section')
    raw_id_fields = ('image',)
    date_hierarchy = 'published'
    list_filter = ('modified', 'published',)
