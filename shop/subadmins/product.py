from django.forms.models import ModelForm
from shop.submodels.product import ProductModel
from django.contrib.admin import ModelAdmin, register
from django.utils.safestring import mark_safe


class _ProductModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_ProductModelForm, self).__init__(*args, **kwargs)
        self.fields['total_sales'].required = True
        self.fields['category'].required = True
        self.fields['price'].required = True
        self.fields['product_preview'].required = True
        self.fields['product_images'].required = True
        self.fields['keywords'].required = True
        self.fields['description'].required = True

    class Meta:
        model = ProductModel
        fields = '__all__'


@register(ProductModel)
class ProductModelAdmin(ModelAdmin):
    form = _ProductModelForm
    list_display = ('title', 'product_preview',)
    raw_id_fields = ('product_preview', 'price', )
    filter_horizontal = ('category', 'product_images', 'reviews',)
    list_filter = ('created_at', 'modified_date',)
    readonly_fields = ('created_at', 'modified_date', 'product_image_preview',)
    date_hierarchy = 'created_at'
    search_fields = ('title', 'total_sales',
                     'description', 'keywords',
                     'price__was',
                     'price__now',
                     'category__title', 'category__description',
                     )
    fieldsets = (
        (None, {
            'fields': ('title', 'category', 'keywords', 'total_sales', 'price',
                       'description', ),
        }),
        ('Preview', {
            'fields': ('product_preview', 'product_image_preview',
                       ),
        }),
        ('Product gallery', {
            'fields': ('product_images',
                       ),
        }),
        ('Product reviews', {
            'fields': ('reviews',
                       ),
        }),
        (None, {
            'fields': ('created_at', 'modified_date',),
        }),
    )

    def product_image_preview(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.product_preview.image.url,
        ))
