from django.forms import ModelForm
from footer.models import FooterSectionModel
from django.contrib.admin import ModelAdmin, register
from django.utils.safestring import mark_safe


class _FooterSectionModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_FooterSectionModelForm, self).__init__(*args, **kwargs)
        self.fields['background_image'].required = True
        self.fields['section_image'].required = True

    class Meta:
        model = FooterSectionModel
        fields = '__all__'


@register(FooterSectionModel)
class FooterSectionModelAdmin(ModelAdmin):
    form = _FooterSectionModelForm
    list_display = ('footer_text', 'footer_logo', 'section_image', 'background_image',  'modified_date',
                    'created_at', )
    raw_id_fields = ('footer_logo', 'background_image', 'section_image',)
    date_hierarchy = 'created_at'
    readonly_fields = ('modified_date',
                       'created_at', 'section_image_preview',
                       'background_image_preview', 'footer_logo_preview',)
    fieldsets = (
        (None, {
            'fields': ('footer_text',),
        }),
        ('Preview', {
            'fields': (
                'footer_logo', 'footer_logo_preview',
                'section_image', 'section_image_preview',
                'background_image', 'background_image_preview',
            ),
        }),
        (None, {
            'fields': ('created_at', 'modified_date',),
        }),
    )

    def footer_logo_preview(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.footer_logo.image.url,
        ))

    def section_image_preview(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.section_image.image.url,
        ))

    def background_image_preview(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.background_image.image.url,
        ))

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and FooterSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
