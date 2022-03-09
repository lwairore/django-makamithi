from service.models import VideoModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm


class _VideoModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_VideoModelForm, self).__init__(*args, **kwargs)
        self.fields['thumbnail'].required = True
        self.fields['caption'].required = True

    class Meta:
        model = VideoModel
        fields = '__all__'


@register(VideoModel)
class VideoModelAdmin(ModelAdmin):
    form = _VideoModelForm
    list_display = ('title', 'thumbnail', 'video', 'modified_date',
                    'created_at', )
    date_hierarchy = 'created_at'
    raw_id_fields = ('thumbnail',)
    readonly_fields = ('modified_date',
                       'created_at', )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and VideoModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
