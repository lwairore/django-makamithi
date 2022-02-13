from home_two.submodels import (PhotoModel, CoreValueModel)
from rest_framework.serializers import ModelSerializer


class _RetrievePhotoModelSerializer(ModelSerializer):
    class Meta:
        model = PhotoModel
        fields = ('image', 'caption',)


class CoreValueModelSerializer(ModelSerializer):
    class Meta:
        model = CoreValueModel
        fields = ('title', 'description', 'image', 'id',)
