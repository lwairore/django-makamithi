from home_two.submodels.about_section import AboutSectionModel
from django.contrib.admin import ModelAdmin, register


@register(AboutSectionModel)
class AboutSectionModelAdmin(ModelAdmin):
    list_display = ('heading', 'subheading', 'photo',)
    raw_id_fields = ('photo',)

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and AboutSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
