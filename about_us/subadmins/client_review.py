from about_us.models import ClientReviewModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm
from django.utils.safestring import mark_safe


class _ClientReviewModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_ClientReviewModelForm, self).__init__(*args, **kwargs)
        self.fields['position'].required = True
        self.fields['image'].required = True

    class Meta:
        model = ClientReviewModel
        fields = '__all__'


@register(ClientReviewModel)
class ClientReviewModelAdmin(ModelAdmin):
    form = _ClientReviewModelForm
    readonly_fields = ('created_at', 'modified_date', 'image_preview',)
    list_display = ('full_name', 'position', 'image', 'modified_date',
                    'created_at', )
    search_fields = ('full_name', 'image', 'review', 'position',)
    raw_id_fields = ('image',)
    date_hierarchy = 'created_at'
    list_filter = ('modified_date', 'created_at',)
    fieldsets = (
        (None, {
            'fields': ('full_name', 'position', 'review',),
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
