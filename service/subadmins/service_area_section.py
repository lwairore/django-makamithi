from service.models import ServiceAreaSectionModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm
from django.utils.safestring import mark_safe


class _ServiceAreaSectionModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_ServiceAreaSectionModelForm, self).__init__(*args, **kwargs)
        self.fields['years_of_experience_image'].required = True
        self.fields['description'].required = True

    class Meta:
        model = ServiceAreaSectionModel
        fields = '__all__'


@register(ServiceAreaSectionModel)
class ServiceAreaSectionModelAdmin(ModelAdmin):
    form = _ServiceAreaSectionModelForm
    list_display = ('heading', 'years_of_experience_image', 'modified_date',
                    'created_at', )
    date_hierarchy = 'created_at'
    raw_id_fields = ('years_of_experience_image',)
    readonly_fields = ('modified_date',
                       'created_at', 'years_of_experience_image_preview',)
    fieldsets = (
        (None, {
            'fields': ('heading', 'description',),
        }),
        ('Preview', {
            'fields': ('years_of_experience_image', 'years_of_experience_image_preview',
                       ),
        }),
        (None, {
            'fields': ('created_at', 'modified_date',),
        }),
    )

    def years_of_experience_image_preview(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.years_of_experience_image.image.url,
        ))

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and ServiceAreaSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
