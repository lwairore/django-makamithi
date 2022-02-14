from about_us.submodels.faq_section import FaqSectionModel
from home_two.models import PhotoModel
from rest_framework.serializers import ModelSerializer


class RetrieveFaqSectionModelSerializer(ModelSerializer):
    class Meta:
        model = FaqSectionModel
        fields = ('title', 'background_image',)
