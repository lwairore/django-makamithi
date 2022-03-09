from service.submodels.service import ServiceModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm
from django.utils.safestring import mark_safe


class _ServiceModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_ServiceModelForm, self).__init__(*args, **kwargs)
        self.fields['keywords'].required = True
        self.fields['summary'].required = True
        self.fields['description'].required = True
        self.fields['home_photo'].required = True
        self.fields['about_photo'].required = True
        self.fields['service_page_photo'].required = True
        self.fields['service_detail_photo'].required = True
        self.fields['nav_sidebar_photo'].required = True
        self.fields['plans'].required = True

    class Meta:
        model = ServiceModel
        fields = '__all__'


@register(ServiceModel)
class ServiceModelAdmin(ModelAdmin):
    form = _ServiceModelForm
    list_display = ('title', 'keywords', 'home_photo', 'about_photo', 'nav_sidebar_photo',
                    'service_page_photo', 'service_detail_photo', 'created_at', 'modified_date',)
    readonly_fields = ('created_at', 'modified_date', 'home_photo_preview',
                       'about_photo_preview',
                       'service_page_photo_preview',
                       'service_detail_photo_preview',
                       'nav_sidebar_photo_preview',)
    search_fields = ('title', 'summary', 'keywords',)
    raw_id_fields = ('home_photo', 'about_photo', 'nav_sidebar_photo',
                     'service_page_photo', 'service_detail_photo',)
    date_hierarchy = 'modified_date'
    list_filter = ('created_at', 'modified_date',)
    filter_horizontal = ('plans',)
    fieldsets = (
        (None, {
            'fields': ('title', 'keywords', 'plans','summary', 'description',),
        }),
        ('Images', {
            'fields': ('home_photo', 'home_photo_preview',
                       'about_photo', 'about_photo_preview',
                       'service_page_photo', 'service_page_photo_preview',
                       'service_detail_photo', 'service_detail_photo_preview',
                       'nav_sidebar_photo', 'nav_sidebar_photo_preview',
                       ),
        }),
        (None, {
            'fields': ('created_at', 'modified_date',),
        }),
    )

    def home_photo_preview(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.home_photo.image.url,
        ))

    def about_photo_preview(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.about_photo.image.url,
        ))

    def service_page_photo_preview(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.service_page_photo.image.url,
        ))

    def service_detail_photo_preview(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.service_detail_photo.image.url,
        ))

    def nav_sidebar_photo_preview(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.nav_sidebar_photo.image.url,
        ))
