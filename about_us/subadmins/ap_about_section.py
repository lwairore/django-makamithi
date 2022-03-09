from about_us.models import ApAboutSectionModel
from django.contrib.admin import ModelAdmin, register
from django.utils.safestring import mark_safe
from django.forms import ModelForm


class _ApAboutSectionModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_ApAboutSectionModelForm, self).__init__(*args, **kwargs)
        self.fields['description'].required = True
        self.fields['section_image'].required = True

    class Meta:
        model = ApAboutSectionModel
        fields = '__all__'


@register(ApAboutSectionModel)
class ApAboutSectionModelAdmin(ModelAdmin):
    form = _ApAboutSectionModelForm
    list_display = ('heading', 'subheading', 'section_image', 'modified_date',
                    'created_at', )
    date_hierarchy = 'created_at'
    raw_id_fields = ('section_image',)
    readonly_fields = ('created_at', 'modified_date', 'section_image_preview',)
    fieldsets = (
        (None, {
            'fields': ('heading', 'subheading', 'description',),
        }),
        ('Preview', {
            'fields': ('section_image', 'section_image_preview',
                       ),
        }),
        (None, {
            'fields': ('created_at', 'modified_date',),
        }),
    )

    def section_image_preview(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.section_image.image.url,
        ))


    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and ApAboutSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
