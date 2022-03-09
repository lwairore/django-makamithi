from home_two.submodels.why_choose_us_section import WhyChooseUsSectionModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm


class _WhyChooseUsSectionModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_WhyChooseUsSectionModelForm, self).__init__(*args, **kwargs)
        self.fields['section_image'].required = True
        self.fields['description'].required = True

    class Meta:
        model = WhyChooseUsSectionModel
        fields = '__all__'


@register(WhyChooseUsSectionModel)
class WhyChooseUsSectionModelAdmin(ModelAdmin):
    form = _WhyChooseUsSectionModelForm
    list_display = ('heading', 'section_image', 'modified_date', 'created_at',)
    list_filter = ('modified_date', 'created_at',)
    search_fields = ('heading', 'description',)
    date_hierarchy = 'created_at'
    raw_id_fields = ('section_image',)
    readonly_fields = ('modified_date', 'created_at',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and WhyChooseUsSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
