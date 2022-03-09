from about_us.models import FaqSectionModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm


class _FaqSectionModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_FaqSectionModelForm, self).__init__(*args, **kwargs)
        self.fields['background_image'].required = True

    class Meta:
        model = FaqSectionModel
        fields = '__all__'


@register(FaqSectionModel)
class FaqSectionModelAdmin(ModelAdmin):
    form = _FaqSectionModelForm
    readonly_fields = ('created_at', 'modified_date',)
    list_display = ('heading', 'background_image', 'modified_date',
                    'created_at', )
    raw_id_fields = ('background_image',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and FaqSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
