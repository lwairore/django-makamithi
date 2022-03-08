from django.forms import ModelForm
from footer.models import FooterSectionModel
from django.contrib.admin import ModelAdmin, register


class _FooterSectionModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_FooterSectionModelForm, self).__init__(*args, **kwargs)
        self.fields['background_image'].required = True
        self.fields['section_image'].required = True

    class Meta:
        model = FooterSectionModel
        fields = '__all__'


@register(FooterSectionModel)
class FooterSectionModelAdmin(ModelAdmin):
    form = _FooterSectionModelForm
    list_display = ('footer_text', 'footer_logo', 'section_image', 'background_image',  'modified_date',
                    'created_at', )
    raw_id_fields = ('footer_logo', 'background_image', 'section_image',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and FooterSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
