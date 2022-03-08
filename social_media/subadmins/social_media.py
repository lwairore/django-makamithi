from django.forms import ModelForm
from social_media.models import SocialMediaModel
from django.contrib.admin import ModelAdmin, register


class _SocialMediaModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_SocialMediaModelForm, self).__init__(*args, **kwargs)
        self.fields['icon'].required = True

    class Meta:
        model = SocialMediaModel
        fields = '__all__'


@register(SocialMediaModel)
class SocialMediaModelAdmin(ModelAdmin):
    form = _SocialMediaModelForm
    list_display = ('title', 'link', 'modified_date', 'created_at',)
    date_hierarchy = 'created_at'
    list_filter = ('modified_date', 'created_at',)
    search_fields = ('title', 'link',)
