from gallery.submodels import GalleryModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm
from django.utils.safestring import mark_safe


class _GalleryModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_GalleryModelForm, self).__init__(*args, **kwargs)
        self.fields['home_preview'].required = True
        self.fields['gallery_preview'].required = True
        self.fields['category'].required = True
        self.fields['title'].required = True
        self.fields['occured_on'].required = True
        self.fields['layout_image'].required = True
        self.fields['description'].required = True
        self.fields['keywords'].required = True

    class Meta:
        model = GalleryModel
        fields = '__all__'


@register(GalleryModel)
class GalleryModelAdmin(ModelAdmin):
    form = _GalleryModelForm
    list_display = ('title', 'category', 'home_preview',
                    'gallery_preview', 'layout_image', 'occured_on', 'modified_date', 'created_at',)
    date_hierarchy = 'created_at'
    raw_id_fields = ('home_preview', 'category',
                     'gallery_preview', 'layout_image',)
    list_filter = ('occured_on', 'modified_date', 'created_at',)
    readonly_fields = ('modified_date', 'created_at',
                       'gallery_preview_image', 'home_preview_image', 'layout_image_preview',)
    search_fields = ('title', 'category', 'occured_on',
                     'keywords', 'description',)
    fieldsets = (
        (None, {
            'fields': ('title', 'keywords', 'category', 'occured_on', 'description',),
        }),
        ('Preview', {
            'fields': ('gallery_preview', 'gallery_preview_image',
                       'home_preview', 'home_preview_image',
                       'layout_image', 'layout_image_preview',
                       ),
        }),
        (None, {
            'fields': ('created_at', 'modified_date',),
        }),
    )

    def gallery_preview_image(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.gallery_preview.image.url,
        ))

    def home_preview_image(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.home_preview.image.url,
        ))

    def layout_image_preview(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.layout_image.image.url,
        ))
