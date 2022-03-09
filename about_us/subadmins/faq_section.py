from about_us.models import FaqSectionModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm
from django.utils.safestring import mark_safe


class _FaqSectionModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_FaqSectionModelForm, self).__init__(*args, **kwargs)
        self.fields['background_image'].required = True

    class Meta:
        model = FaqSectionModel
        fields = '__all__'


@register(FaqSectionModel)
class FaqSectionModelAdmin(ModelAdmin):
    form = _FaqSectionModelForm
    readonly_fields = ('created_at', 'modified_date',
                       'background_image_preview',)
    list_display = ('heading', 'background_image', 'modified_date',
                    'created_at', )
    raw_id_fields = ('background_image',)
    fieldsets = (
        (None, {
            'fields': ('heading',),
        }),
        ('Preview', {
            'fields': (
                'background_image', 'background_image_preview',
            ),
        }),
        (None, {
            'fields': ('created_at', 'modified_date',),
        }),
    )

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
        if should_add_instance and FaqSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
