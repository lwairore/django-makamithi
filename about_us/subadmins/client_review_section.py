from about_us.models import ClientReviewSectionModel
from django.contrib.admin import ModelAdmin, register


@register(ClientReviewSectionModel)
class ClientReviewSectionModelAdmin(ModelAdmin):
    list_display = ('heading', 'section_image', 'background_image', 'modified_date',
                    'created_at', )
    raw_id_fields = ('section_image',)

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and ClientReviewSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
