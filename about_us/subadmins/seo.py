from about_us.models import AboutUsSEODetailsModel
from social_sharing.subadmins.seo_social_share_data import SeoSocialShareDataModelAdmin
from django.contrib.admin import register


@register(AboutUsSEODetailsModel)
class AboutUsSEODetailsModelAdmin(SeoSocialShareDataModelAdmin):
    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and AboutUsSEODetailsModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance

    def has_delete_permission(self, request, obj=None):
        return False
