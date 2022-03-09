from django.forms import ModelForm
from home_two.submodels.about_section import AboutSectionModel
from django.contrib.admin import ModelAdmin, register
from django.utils.safestring import mark_safe


class _AboutSectionModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_AboutSectionModelForm, self).__init__(*args, **kwargs)
        self.fields['subheading'].required = True
        self.fields['description'].required = True
        self.fields['photo'].required = True

    class Meta:
        model = AboutSectionModel
        fields = '__all__'


@register(AboutSectionModel)
class AboutSectionModelAdmin(ModelAdmin):
    form = _AboutSectionModelForm
    list_display = ('heading', 'subheading', 'photo',
                    'modified_date', 'created_at',)
    raw_id_fields = ('photo',)
    date_hierarchy = 'created_at'
    readonly_fields = ('modified_date', 'created_at', 'photo_preview',)
    fieldsets = (
        (None, {
            'fields': ('heading', 'subheading', 'description'),
        }),
        ('Preview', {
            'fields': ('photo', 'photo_preview',
                       ),
        }),
        (None, {
            'fields': ('created_at', 'modified_date',),
        }),
    )

    def photo_preview(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.photo.image.url,
        ))

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and AboutSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance

    def has_delete_permission(self, request, obj=None):
        return False
