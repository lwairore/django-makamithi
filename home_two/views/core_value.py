from home_two.serializers.core_value import CoreValueModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class CoreValueAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = CoreValueModelSerializer
