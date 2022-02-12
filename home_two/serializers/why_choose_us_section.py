from home_two.submodels import WhyChooseUsSectionModel
from rest_framework.serializers import ModelSerializer


class RetrieveWhyChooseUsSectionSerializer(ModelSerializer):
    class Meta:
        model = WhyChooseUsSectionModel
        fields = ('heading', 'description', 'section_image',)
