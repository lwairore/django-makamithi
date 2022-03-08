from django.forms import ModelForm
from contact_us.models import LeaveUsAMessageSectionModel
from django.contrib.admin import ModelAdmin, register


class _LeaveUsAMessageSectionModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_LeaveUsAMessageSectionModelForm, self).__init__(*args, **kwargs)
        self.fields['our_promise'].required = True

    class Meta:
        model = LeaveUsAMessageSectionModel
        fields = '__all__'


@register(LeaveUsAMessageSectionModel)
class LeaveUsAMessageSectionModelAdmin(ModelAdmin):
    list_display = ('heading', 'background_image', 'modified_date',
                    'created_at', )
    raw_id_fields = ('background_image',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and LeaveUsAMessageSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
