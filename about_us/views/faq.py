from about_us.models import FaqModel
from about_us.serializers.faq import RetrieveFaqModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class ListFaqModelAPIView(APIView):
    permission_classes = (AllowAny,)