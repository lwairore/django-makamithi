from about_us.models import TeamAreaSectionModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm


class _TeamAreaSectionModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_TeamAreaSectionModelForm, self).__init__(*args, **kwargs)
        self.fields['section_image'].required = True
        self.fields['summary'].required = True

    class Meta:
        model = TeamAreaSectionModel
        fields = '__all__'


@register(TeamAreaSectionModel)
class TeamAreaSectionModelAdmin(ModelAdmin):
    form = _TeamAreaSectionModelForm
    list_display = ('heading', 'section_image', 'modified_date',
                    'created_at', )
    raw_id_fields = ('section_image',)
    date_hierarchy = 'created_at'
    readonly_fields = ('modified_date',
                       'created_at',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and TeamAreaSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
