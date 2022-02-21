from home_two.submodels.preview_item import PhotoModel
from service.models import ServiceAreaSectionModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveServiceAreaSectionModelSerializer(ModelSerializer):
    years_of_experience_image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = ServiceAreaSectionModel
        fields = ('heading', 'description',
                  'years_of_experience_image',)
