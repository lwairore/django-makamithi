from about_us.models import ClientReviewSectionModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm
from django.utils.safestring import mark_safe


class _ClientReviewSectionModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_ClientReviewSectionModelForm, self).__init__(*args, **kwargs)
        self.fields['background_image'].required = True
        self.fields['section_image'].required = True
        self.fields['summary'].required = True

    class Meta:
        model = ClientReviewSectionModel
        fields = '__all__'


@register(ClientReviewSectionModel)
class ClientReviewSectionModelAdmin(ModelAdmin):
    form = _ClientReviewSectionModelForm
    list_display = ('heading', 'section_image', 'background_image', 'modified_date',
                    'created_at', )
    raw_id_fields = ('section_image', 'background_image',)
    readonly_fields = ('created_at', 'modified_date', 'section_image_preview',
                       'background_image_preview',)
    fieldsets = (
        (None, {
            'fields': ('heading', 'summary',),
        }),
        ('Preview', {
            'fields': ('section_image', 'section_image_preview',
                       'background_image', 'background_image_preview',
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
        if should_add_instance and ClientReviewSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
