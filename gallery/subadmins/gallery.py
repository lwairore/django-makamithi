from gallery.submodels import GalleryModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm


class GalleryModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(GalleryModelForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = True

    class Meta:
        model = GalleryModel
        fields = '__all__'


@register(GalleryModel)
class GalleryModelAdmin(ModelAdmin):
    form = GalleryModelForm
    list_display = ('id', 'image',)
    date_hierarchy = 'created_at'
    raw_id_fields = ('image',)
    list_filter = ('modified_date', 'created_at',)
