from shop.submodels.product_category import ProductCategoryModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm


class _ProductCategoryModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_ProductCategoryModelForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = True

    class Meta:
        model = ProductCategoryModel
        fields = '__all__'


@register(ProductCategoryModel)
class ProductCategoryModelAdmin(ModelAdmin):
    form = _ProductCategoryModelForm
    list_display = ('title', 'created_at', 'modified_date',)
    date_hierarchy = 'created_at'
    readonly_fields = ('created_at', 'modified_date',)
    list_filter = ('created_at', 'modified_date',)
    search_fields = ('title', 'description',)
