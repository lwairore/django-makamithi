from about_us.models import ClientReviewModel
from django.contrib.admin import ModelAdmin, register
from django.forms import ModelForm


class _ClientReviewModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(_ClientReviewModelForm, self).__init__(*args, **kwargs)
        self.fields['position'].required = True
        self.fields['image'].required = True

    class Meta:
        model = ClientReviewModel
        fields = '__all__'


@register(ClientReviewModel)
class ClientReviewModelAdmin(ModelAdmin):
    form = _ClientReviewModelForm
    readonly_fields = ('created_at', 'modified_date',)
    list_display = ('full_name', 'position', 'image', 'modified_date',
                    'created_at', )
    search_fields = ('full_name', 'image', 'review', 'position',)
    raw_id_fields = ('image',)
    date_hierarchy = 'created_at'
    list_filter = ('modified_date', 'created_at',)
