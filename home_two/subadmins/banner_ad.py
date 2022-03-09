from django.forms import ModelForm
from home_two.submodels.banner_ad import BannerAdModel
from django.contrib.admin import ModelAdmin, register
from django.utils.safestring import mark_safe


class _BannerAdModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_BannerAdModelForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = True
        self.fields['photo'].required = True

    class Meta:
        model = BannerAdModel
        fields = '__all__'


@register(BannerAdModel)
class BannerAdModelAdmin(ModelAdmin):
    form = _BannerAdModelForm
    list_display = ('title', 'photo',)
    raw_id_fields = ('photo',)
    date_hierarchy = 'created_at'
    search_fields = ('title', 'description',)
    list_filter = ('modified_date', 'created_at',)
    readonly_fields = ('modified_date',
                       'created_at', 'photo_preview',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description',),
        }),
        ('Preview', {
            'fields': ('photo', 'photo_preview',
                       ),
        }),
        (None, {
            'fields': ('created_at', 'modified_date',),
        }),
    )

    def photo_preview(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.photo.image.url,
        ))
