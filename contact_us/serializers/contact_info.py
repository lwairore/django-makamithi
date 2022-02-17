from home_two.submodels.preview_item import PhotoModel
from contact_us.submodels.contact_info import ContactInfoModel
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveContactInfoModelSerializer(ModelSerializer):
    address_image = _RetrievePhotoModelSerializer(required=False)
    
    class Meta:
        model = ContactInfoModel
        fields = (
            'address_title',
            'address_image',
            'address',
            'email',
            'phone_number', )
