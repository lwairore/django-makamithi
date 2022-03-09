from service.models import ServiceAboutSectionModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm


class _ServiceAboutSectionModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_ServiceAboutSectionModelForm, self).__init__(*args, **kwargs)
        self.fields['summary'].required = True
        self.fields['section_image'].required = True

    class Meta:
        model = ServiceAboutSectionModel
        fields = '__all__'


@register(ServiceAboutSectionModel)
class ServiceAboutSectionModelAdmin(ModelAdmin):
    form = _ServiceAboutSectionModelForm
    list_display = ('heading', 'section_image', 'modified_date',
                    'created_at', )
    date_hierarchy = 'created_at'
    raw_id_fields = ('section_image',)
    readonly_fields = ('modified_date',
                       'created_at', )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and ServiceAboutSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
