from about_us.models import ClientReviewSectionModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm


class _ClientReviewSectionModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_ClientReviewSectionModelForm, self).__init__(*args, **kwargs)
        self.fields['background_image'].required = True
        self.fields['section_image'].required = True
        self.fields['summary'].required = True

    class Meta:
        model = ClientReviewSectionModel
        fields = '__all__'


@register(ClientReviewSectionModel)
class ClientReviewSectionModelAdmin(ModelAdmin):
    form = _ClientReviewSectionModelForm
    list_display = ('heading', 'section_image', 'background_image', 'modified_date',
                    'created_at', )
    raw_id_fields = ('section_image', 'background_image',)
    readonly_fields = ('created_at', 'modified_date',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and ClientReviewSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
