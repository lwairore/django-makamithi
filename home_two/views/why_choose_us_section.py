from home_two.serializers.why_choose_us_section import RetrieveWhyChooseUsSectionSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class RetrieveWhyChooseUsSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveWhyChooseUsSectionSerializer