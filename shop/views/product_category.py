from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class ListProductCategoryAPIView(APIView):
    permission_classes = (AllowAny,)