from django.forms.models import ModelForm
from shop.models import ProductReview
from django.contrib.admin import ModelAdmin, register


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
    readonly_fields = ('created_at', 'modified_date',)
    date_hierarchy = 'created_at'
    search_fields = ('full_name', 'review', )
