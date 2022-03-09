from home_two.submodels import CoreValueModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm
from django.utils.safestring import mark_safe


class _CoreValueModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_CoreValueModelForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = True
        self.fields['description'].required = True

    class Meta:
        model = CoreValueModel
        fields = '__all__'


@register(CoreValueModel)
class CoreValueModelAdmin(ModelAdmin):
    form = _CoreValueModelForm
    list_display = ('title', 'image', 'created_at', 'modified_date')
    search_fields = ('title', 'description',)
    list_filter = ('created_at', 'modified_date',)
    readonly_fields = ('created_at', 'modified_date', 'image_preview',)
    date_hierarchy = 'created_at'
    raw_id_fields = ('image',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description',),
        }),
        ('Preview', {
            'fields': ('image', 'image_preview',
                       ),
        }),
        (None, {
            'fields': ('created_at', 'modified_date',),
        }),
    )

    def image_preview(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.image.image.url,
        ))
