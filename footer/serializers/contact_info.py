from contact_us.submodels.contact_info import ContactInfoModel
from rest_framework.serializers import ModelSerializer


class RetrieveContactInfoModelSerializer(ModelSerializer):

    class Meta:
        model = ContactInfoModel
        fields = (
            'address_title',
            'address',
            'email',
            'phone_number', )
