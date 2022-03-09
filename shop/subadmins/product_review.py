from django.forms.models import ModelForm
from shop.models import ProductReview
from django.contrib.admin import ModelAdmin, register
from django.utils.safestring import mark_safe


class _ProductReviewForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_ProductReviewForm, self).__init__(*args, **kwargs)
        self.fields['client_image'].required = True

    class Meta:
        model = ProductReview
        fields = '__all__'


@register(ProductReview)
class ProductReviewAdmin(ModelAdmin):
    form = _ProductReviewForm
    list_display = ('full_name', 'rating', 'client_image',)
    raw_id_fields = ('client_image', )
    list_filter = ('created_at', 'modified_date',)
    readonly_fields = ('created_at', 'modified_date', 'client_image_preview')
    date_hierarchy = 'created_at'
    search_fields = ('full_name', 'review', )
    fieldsets = (
        (None, {
            'fields': ('full_name',),
        }),
        ('Image', {
            'fields': ('client_image', 'client_image_preview',
                       ),
        }),
        (None, {
            'fields': ('review', 'rating',),
        }),
        (None, {
            'fields': ('created_at', 'modified_date',),
        }),
    )

    def client_image_preview(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.client_image.image.url,
        ))
