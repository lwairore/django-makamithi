from service.submodels.service import ServiceModel
from rest_framework.serializers import ModelSerializer


class RetrieveServiceModelSerializer(ModelSerializer):
    class Meta:
        model = ServiceModel
        fields = ('photo', 'id', 'title', 'summary')
