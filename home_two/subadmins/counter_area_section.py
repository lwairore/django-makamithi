from django.forms import ModelForm
from home_two.submodels import CounterAreaSectionModel
from django.contrib.admin import ModelAdmin, register


class _CounterAreaSectionModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_CounterAreaSectionModelForm, self).__init__(*args, **kwargs)
        self.fields['background_image'].required = True

    class Meta:
        model = CounterAreaSectionModel
        fields = '__all__'


@register(CounterAreaSectionModel)
class CounterAreaSectionModelAdmin(ModelAdmin):
    form = _CounterAreaSectionModelForm
    date_hierarchy = 'created_at'
    list_display = ('heading', 'background_image',
                    'modified_date', 'created_at',)
    raw_id_fields = ('background_image',)

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and CounterAreaSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance

    def has_delete_permission(self, request, obj=None):
        return False
