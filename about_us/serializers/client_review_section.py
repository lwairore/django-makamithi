from home_two.submodels.preview_item import PhotoModel
from about_us.submodels.client_review_section import ClientReviewSectionModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveClientReviewSectionModelSerializer(ModelSerializer):
    section_image = _RetrievePhotoModelSerializer(required=False)

    class Meta:
        model = ClientReviewSectionModel
        fields = ('heading', 'summary',
                  'section_image',)
