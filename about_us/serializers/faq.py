from about_us.models import FaqModel
from rest_framework.serializers import ModelSerializer


class RetrieveFaqModelSerializer(ModelSerializer):
    class Meta:
        model = FaqModel
        fields = ('question', 'answer',)
