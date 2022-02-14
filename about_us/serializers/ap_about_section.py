from about_us.submodels.ap_about_section import ApAboutSectionModel
from rest_framework.serializers import ModelSerializer


class ApAboutSectionModelSerializer(ModelSerializer):
    class Meta:
        model = ApAboutSectionModel
        fields = ('heading', 'subheading', 'description',
                  'section_image',)
