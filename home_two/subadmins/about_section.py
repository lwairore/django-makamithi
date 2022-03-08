from django.forms import ModelForm
from home_two.submodels.about_section import AboutSectionModel
from django.contrib.admin import ModelAdmin, register

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
    list_display = ('heading', 'subheading', 'photo',)
    raw_id_fields = ('photo',)

    def has_add_permission(self, request):
        # check if generally has add permission
        should_add_instance = super().has_add_permission(request)
        # set add permission to False, if object already exists
        if should_add_instance and AboutSectionModel.objects.only('pk').exists():
            should_add_instance = False

        return should_add_instance

    def has_delete_permission(self, request, obj=None):
        return False