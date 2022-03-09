from gallery.models import GalleryDetailSectionModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm


class _GalleryDetailSectionModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_GalleryDetailSectionModelForm, self).__init__(*args, **kwargs)
        self.fields['background_image'].required = True

    class Meta:
        model = GalleryDetailSectionModel
        fields = '__all__'


@register(GalleryDetailSectionModel)
class GalleryDetailSectionModelAdmin(ModelAdmin):
    form = _GalleryDetailSectionModelForm
    list_display = ('background_image', 'modified_date',
                    'created_at', )
    raw_id_fields = ('background_image',)
    date_hierarchy = 'created_at'
    readonly_fields = ('modified_date',
                       'created_at', )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and GalleryDetailSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
