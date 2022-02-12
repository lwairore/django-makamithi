from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class RetrievewhyChooseUsSectionAPIView(APIView):
    permission_classes = (AllowAny,)
