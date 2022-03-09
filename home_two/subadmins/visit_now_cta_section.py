from home_two.submodels.visit_now_cta_section import VisitNowCtaSectionModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm


class _VisitNowCtaSectionModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_VisitNowCtaSectionModelForm, self).__init__(*args, **kwargs)
        self.fields['background_image'].required = True
        self.fields['section_image'].required = True
        self.fields['description'].required = True

    class Meta:
        model = VisitNowCtaSectionModel
        fields = '__all__'


@register(VisitNowCtaSectionModel)
class VisitNowCtaSectionModelAdmin(ModelAdmin):
    form = _VisitNowCtaSectionModelForm
    list_display = ('heading', 'background_image',
                    'section_image', 'modified_date', 'created_at',)
    date_hierarchy = 'created_at'
    raw_id_fields = ('background_image', 'section_image',)
    readonly_fields = ('modified_date', 'created_at',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and VisitNowCtaSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
