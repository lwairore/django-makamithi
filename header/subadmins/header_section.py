from header.models import HeaderSectionModel
from django.contrib.admin import ModelAdmin, register


@register(HeaderSectionModel)
class HeaderSectionModelAdmin(ModelAdmin):
    list_display = ('primary_location', 'whatsapp_business_number', 'primary_email', 'logo_side', 'standard_logo', 'retina_logo', 'modified_date',
                    'created_at', )
    raw_id_fields = ('logo_side', 'standard_logo', 'retina_logo',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and HeaderSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
