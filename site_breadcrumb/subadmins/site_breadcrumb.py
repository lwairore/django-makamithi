from site_breadcrumb.models import SiteBreadcrumbModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm


class _SiteBreadcrumbModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_SiteBreadcrumbModelForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = True

    class Meta:
        model = SiteBreadcrumbModel
        fields = '__all__'


@register(SiteBreadcrumbModel)
class SiteBreadcrumbModelAdmin(ModelAdmin):
    form = _SiteBreadcrumbModelForm
    list_display = ('id', 'image',)
    date_hierarchy = 'created_at'
    raw_id_fields = ('image',)
    list_filter = ('modified_date', 'created_at',)