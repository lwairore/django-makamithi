from about_us.submodels.what_we_do_section import WhatWeDoSectionModel
from rest_framework.serializers import ModelSerializer


class RetrieveWhatWeDoSectionModelSerializer(ModelSerializer):

    class Meta:
        model = WhatWeDoSectionModel
        fields = ('heading', 'summary',
                  'section_image',)
