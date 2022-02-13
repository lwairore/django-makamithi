from site_breadcrumb.models import SiteBreadcrumbModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm


class SiteBreadcrumbModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SiteBreadcrumbModelForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = True

    class Meta:
        model = SiteBreadcrumbModel
        fields = '__all__'
