from social_sharing.submodels.seo_social_share_data import SeoSocialShareDataModel
from django.contrib.admin import ModelAdmin
from django.utils.safestring import mark_safe
from django.forms import ModelForm


class _SeoSocialShareDataModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_SeoSocialShareDataModelForm, self).__init__(*args, **kwargs)
        self.fields['keywords'].required = True
        self.fields['description'].required = True
        self.fields['image'].required = True
        self.fields['type'].required = True
        self.fields['author'].required = True
        self.fields['section'].required = True

    class Meta:
        model = SeoSocialShareDataModel
        fields = '__all__'


class SeoSocialShareDataModelAdmin(ModelAdmin):
    form = _SeoSocialShareDataModelForm
    readonly_fields = ('published', 'modified', 'image_preview',)
    list_display = ('title', 'keywords', 'type',
                    'author', 'section', 'published', 'modified',)
    raw_id_fields = ('image',)
    date_hierarchy = 'published'
    fieldsets = (
        (None, {
            'fields': ('title', 'keywords', 'description', 'type', 'author', 'section'),
        }),
        ('Preview', {
            'fields': ('image', 'image_preview',
                       ),
        }),
        (None, {
            'fields': ('published', 'modified',),
        }),
    )

    def image_preview(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.image.image.url,
        ))
