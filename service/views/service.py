from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

class ListServiceAPIView(APIView):
    permission_classes = (AllowAny,)
    
