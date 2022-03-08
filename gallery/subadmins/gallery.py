from gallery.submodels import GalleryModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm


class _GalleryModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_GalleryModelForm, self).__init__(*args, **kwargs)
        self.fields['home_preview'].required = True
        self.fields['gallery_preview'].required = True
        self.fields['category'].required = True
        self.fields['title'].required = True
        self.fields['occured_on'].required = True
        self.fields['layout_image'].required = True

    class Meta:
        model = GalleryModel
        fields = '__all__'


@register(GalleryModel)
class GalleryModelAdmin(ModelAdmin):
    form = _GalleryModelForm
    list_display = ('id', 'title', 'category', 'home_preview',
                    'gallery_preview', 'layout_image', 'occured_on', 'modified_date', 'created_at',)
    date_hierarchy = 'created_at'
    raw_id_fields = ('home_preview', 'category', 'gallery_preview', 'layout_image',)
    list_filter = ('occured_on', 'modified_date', 'created_at',)
    search_fields = ('title', 'category', 'occured_on',
                     'keywords', 'description',)
