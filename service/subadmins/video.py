from service.models import VideoModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm
from django.utils.safestring import mark_safe


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
                       'created_at', 'thumbnail_preview', 'video_preview',)
    fieldsets = (
        (None, {
            'fields': ('title', ),
        }),
        ('Thumbnail', {
            'fields': ('thumbnail', 'thumbnail_preview',
                       ),
        }),
        ('Video', {
            'fields': ('video', 'video_preview',
                       ),
        }),
        (None, {
            'fields': ('caption',
                       ),
        }),
        (None, {
            'fields': ('created_at', 'modified_date',),
        }),
    )

    def thumbnail_preview(self, obj):
        return mark_safe('<img src="{url}" style="max-width: 100%; max-height: 100%;" />'.format(
            url=obj.thumbnail.image.url,
        ))

    def video_preview(self, obj):
        return mark_safe('<video src="{url}" style="max-width: 100%; max-height: 100%;" controls></video>'.format(
            url=obj.video.url,
        ))

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and VideoModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance
