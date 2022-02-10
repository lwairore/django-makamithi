from home_two.submodels.about_section import AboutSectionModel
from rest_framework.serializers import ModelSerializer


class RetrieveAboutSectionSerializer(ModelSerializer):

    class Meta:
        model = AboutSectionModel
        fields = ('heading', 'description', 'photo',)
