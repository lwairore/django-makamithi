from home_two.submodels.about_section import AboutSectionModel
from home_two.submodels.preview_item import PhotoModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveAboutSectionSerializer(ModelSerializer):
    photo = _RetrievePhotoModelModelSerializer(required=False)

    class Meta:
        model = AboutSectionModel
        fields = ('heading', 'description', 'photo',)
