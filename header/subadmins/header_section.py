from header.models import HeaderSectionModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm


class _HeaderSectionModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_HeaderSectionModelForm, self).__init__(*args, **kwargs)
        self.fields['whatsapp_business_number'].required = True

    class Meta:
        model = HeaderSectionModel
        fields = '__all__'

@register(HeaderSectionModel)
class HeaderSectionModelAdmin(ModelAdmin):
    form = _HeaderSectionModelForm
    list_display = ('primary_location', 'whatsapp_business_number', 'primary_email', 'logo_side', 'standard_logo', 'retina_logo', 'modified_date',
                    'created_at', )
    raw_id_fields = ('logo_side', 'standard_logo', 'retina_logo',)
    date_hierarchy = 'created_at'
    readonly_fields = ('modified_date',
                       'created_at', )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and HeaderSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
