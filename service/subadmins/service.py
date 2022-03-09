from service.submodels.service import ServiceModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm


class _ServiceModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_ServiceModelForm, self).__init__(*args, **kwargs)
        self.fields['keywords'].required = True
        self.fields['summary'].required = True
        self.fields['description'].required = True
        self.fields['home_photo'].required = True
        self.fields['about_photo'].required = True
        self.fields['service_page_photo'].required = True
        self.fields['service_detail_photo'].required = True
        self.fields['nav_sidebar_photo'].required = True
        self.fields['plans'].required = True

    class Meta:
        model = ServiceModel
        fields = '__all__'


@register(ServiceModel)
class ServiceModelAdmin(ModelAdmin):
    form = _ServiceModelForm
    list_display = ('title', 'keywords', 'home_photo', 'about_photo', 'nav_sidebar_photo',
                    'service_page_photo', 'service_detail_photo', 'created_at', 'modified_date',)
    readonly_fields = ('created_at', 'modified_date',)
    search_fields = ('title', 'summary', 'keywords',)
    raw_id_fields = ('home_photo', 'about_photo', 'nav_sidebar_photo',
                     'service_page_photo', 'service_detail_photo',)
    date_hierarchy = 'modified_date'
    list_filter = ('created_at', 'modified_date',)
    filter_horizontal = ('plans',)
