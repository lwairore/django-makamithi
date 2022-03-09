from home_two.submodels.preview_item import PhotoModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm
from django.utils.safestring import mark_safe


class _PhotoModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_PhotoModelForm, self).__init__(*args, **kwargs)
        self.fields['width'].required = True
        self.fields['height'].required = True
        self.fields['caption'].required = True

    class Meta:
        model = PhotoModel
        fields = '__all__'


@register(PhotoModel)
class PhotoModelAdmin(ModelAdmin):
    form = _PhotoModelForm
    list_display = ('id', 'image', 'width', 'height',)
    date_hierarchy = 'created_at'
    list_filter = ('modified_date', 'created_at')
    readonly_fields = ('modified_date', 'created_at', 'image_preview')
    search_fields = ('caption', 'width', 'height',)
    fieldsets = (

        ('Image', {
            'fields': ('image', 'image_preview',
                       ),
        }),
         (None, {
            'fields': ('caption',),
        }),
        ('Dimensions', {
            'fields': ('width', 'height',),
        }),
        (None, {
            'fields': ('created_at', 'modified_date',),
        }),
    )

    def image_preview(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.image.url,
        ))
