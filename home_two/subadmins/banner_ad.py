from django.forms import ModelForm
from home_two.submodels.banner_ad import BannerAdModel
from django.contrib.admin import ModelAdmin, register


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
                       'created_at',)
