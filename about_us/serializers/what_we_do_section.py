from home_two.submodels.preview_item import PhotoModel
from about_us.submodels.what_we_do_section import WhatWeDoSectionModel
from rest_framework.serializers import ModelSerializer

class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class RetrieveWhatWeDoSectionModelSerializer(ModelSerializer):
    section_image = _RetrievePhotoModelSerializer(required=False)
    
    class Meta:
        model = WhatWeDoSectionModel
        fields = ('heading', 'summary',
                  'section_image',)
