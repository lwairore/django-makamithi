from home_two.serializers.our_feature_section import RetrieveFeatureSectionSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class RetrieveFeatureSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveFeatureSectionSerializer
    
