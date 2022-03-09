from home_two.submodels.our_feature_section import FeatureSectionModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm


class _FeatureSectionModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_FeatureSectionModelForm, self).__init__(*args, **kwargs)
        self.fields['background_image'].required = True
        self.fields['section_image'].required = True
        self.fields['summary'].required = True

    class Meta:
        model = FeatureSectionModel
        fields = '__all__'


@register(FeatureSectionModel)
class FeatureSectionModelAdmin(ModelAdmin):
    form = _FeatureSectionModelForm
    list_display = ('summary', 'background_image',
                    'section_image', 'created_at', 'modified_date',)
    date_hierarchy = 'created_at'
    raw_id_fields = ('background_image', 'section_image',)
    readonly_fields = ('created_at', 'modified_date',)

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and FeatureSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance

    def has_delete_permission(self, request, obj=None):
        return False
