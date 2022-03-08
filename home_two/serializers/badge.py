from home_two.models import BadgeModel
from rest_framework.serializers import ModelSerializer


class RetrieveBadgeModelSerializer(ModelSerializer):

    class Meta:
        model = BadgeModel
        fields = ('number_of_years', 'title',)
