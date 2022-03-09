from home_two.models import ProductAreaSectionModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm


class _ProductAreaSectionModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_ProductAreaSectionModelForm, self).__init__(*args, **kwargs)
        self.fields['summary'].required = True
        self.fields['section_image'].required = True

    class Meta:
        model = ProductAreaSectionModel
        fields = '__all__'


@register(ProductAreaSectionModel)
class ProductAreaSectionModelAdmin(ModelAdmin):
    form = _ProductAreaSectionModelForm
    list_display = ('heading', 'section_image', 'created_at', 'modified_date',)
    date_hierarchy = 'created_at'
    raw_id_fields = ('section_image',)
    readonly_fields = ('created_at', 'modified_date',)

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and ProductAreaSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance

    def has_delete_permission(self, request, obj=None):
        return False
