from service.models import ServiceSEODetailsModel
from social_sharing.subadmins.seo_social_share_data import SeoSocialShareDataModelAdmin
from django.contrib.admin import register


@register(ServiceSEODetailsModel)
class ServiceSEODetailsModelAdmin(SeoSocialShareDataModelAdmin):
    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and ServiceSEODetailsModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance

    def has_delete_permission(self, request, obj=None):
        return False
