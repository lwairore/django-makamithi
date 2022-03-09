from shop.submodels.price import PriceModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm


class _PriceModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_PriceModelForm, self).__init__(*args, **kwargs)
        self.fields['now'].required = True

    class Meta:
        model = PriceModel
        fields = '__all__'


@register(PriceModel)
class PriceModelAdmin(ModelAdmin):
    form = _PriceModelForm
    list_display = ('now', 'was',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at', 'modified_date',)
    readonly_fields = ('created_at', 'modified_date',)
    search_fields = ('now', 'was',)
