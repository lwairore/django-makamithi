from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class RetrieveVisitNowCtaSectionAPIView(APIView):
    permission_classes = (AllowAny,)
