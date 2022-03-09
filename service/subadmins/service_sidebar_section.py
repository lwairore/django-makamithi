from service.models import ServiceSidebarSectionModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm


class _ServiceSidebarSectionModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_ServiceSidebarSectionModelForm, self).__init__(*args, **kwargs)
        self.fields['background_image'].required = True
        self.fields['summary'].required = True
        self.fields['section_image'].required = True

    class Meta:
        model = ServiceSidebarSectionModel
        fields = '__all__'


@register(ServiceSidebarSectionModel)
class ServiceSidebarSectionModelAdmin(ModelAdmin):
    form = _ServiceSidebarSectionModelForm
    list_display = ('heading', 'background_image', 'section_image', 'modified_date',
                    'created_at', )
    date_hierarchy = 'created_at'
    readonly_fields = ('modified_date',
                       'created_at',)
    raw_id_fields = ('background_image', 'section_image',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and ServiceSidebarSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
