from home_two.submodels.core_value import CoreValueModel
from rest_framework.serializers import ModelSerializer


class CoreValueModelSerializer(ModelSerializer):
    class Meta:
        model = CoreValueModel
        fields = ('title', 'description', 'image', 'id',)
