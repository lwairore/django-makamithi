from site_breadcrumb.models import SiteBreadcrumbModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm


class _SiteBreadcrumbModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_SiteBreadcrumbModelForm, self).__init__(*args, **kwargs)
        self.fields['background_image'].required = True

    class Meta:
        model = SiteBreadcrumbModel
        fields = '__all__'


@register(SiteBreadcrumbModel)
class SiteBreadcrumbModelAdmin(ModelAdmin):
    form = _SiteBreadcrumbModelForm
    list_display = ('id', 'background_image',)
    date_hierarchy = 'created_at'
    raw_id_fields = ('background_image',)
    list_filter = ('modified_date', 'created_at',)

    def has_delete_permission(self, request, obj = None):
        return False
