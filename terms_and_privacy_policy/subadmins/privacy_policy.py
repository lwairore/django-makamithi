from terms_and_privacy_policy.models import PrivacyPolicyModel
from django.contrib.admin import ModelAdmin, register


@register(PrivacyPolicyModel)
class PrivacyPolicyModelAdmin(ModelAdmin):
    list_display = ('section_name', 'modified_date',
                    'created_at', )
    date_hierarchy = 'created_at'

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and PrivacyPolicyModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
