from home_two.submodels import CoreValueModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm


class _CoreValueModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_CoreValueModelForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = True
        self.fields['description'].required = True

    class Meta:
        model = CoreValueModel
        fields = '__all__'


@register(CoreValueModel)
class CoreValueModelAdmin(ModelAdmin):
    form = _CoreValueModelForm
    list_display = ('title', 'image', 'created_at', 'modified_date')
    search_fields = ('title', 'description',)
    list_filter = ('created_at', 'modified_date',)
    readonly_fields = ('created_at', 'modified_date',)
    date_hierarchy = 'created_at'
    raw_id_fields = ('image',)
