from home_two.submodels.our_feature_section import FeatureSectionModel
from rest_framework.serializers import ModelSerializer


class RetrieveFeatureSectionSerializer(ModelSerializer):
    class Meta:
        model = FeatureSectionModel
        fields = ('heading', 'description', 'photo',)
