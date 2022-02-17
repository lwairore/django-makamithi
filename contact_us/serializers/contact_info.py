from contact_us.submodels.contact_info import ContactInfoModel
from rest_framework.serializers import ModelSerializer


class ContactInfoModelSerializer(ModelSerializer):
    class Meta:
        model = ContactInfoModel
        fields = (
            'address_title',
            'address_image',
            'address',
            'email',
            'phone_number', )
