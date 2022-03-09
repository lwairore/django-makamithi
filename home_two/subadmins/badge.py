from django.forms import ModelForm
from home_two.models import BadgeModel
from django.contrib.admin import ModelAdmin, register


class _BadgeModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_BadgeModelForm, self).__init__(*args, **kwargs)
        self.fields['title'].required = True

    class Meta:
        model = BadgeModel
        fields = '__all__'


@register(BadgeModel)
class BadgeModelAdmin(ModelAdmin):
    form = _BadgeModelForm
    list_display = ('title', 'number_of_years', 'created_at', 'modified_date',)
    search_fields = ('title', 'number_of_years',)
    date_hierarchy = 'created_at'
    list_filter = ('created_at', 'modified_date',)
    readonly_fields = ('modified_date',
                       'created_at',)
