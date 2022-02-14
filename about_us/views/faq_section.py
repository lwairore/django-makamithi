from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

class RetrieveFaqSectionAPIView(APIView):
    permission_classes = (AllowAny,)