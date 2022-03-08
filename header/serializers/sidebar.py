from contact_us.submodels.contact_info import ContactInfoModel
from home_two.submodels.preview_item import PhotoModel
from service.submodels.service import ServiceModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveServiceForSidebarSerializer(ModelSerializer):
    nav_sidebar_photo = _RetrievePhotoModelModelSerializer(required=False)

    class Meta:
        model = ServiceModel
        fields = ('nav_sidebar_photo', 'id', 'title',)


class RetrieveContactInfoModelSerializer(ModelSerializer):

    class Meta:
        model = ContactInfoModel
        fields = (
            'address_title',
            'address',
            'email',
            'phone_number', )
