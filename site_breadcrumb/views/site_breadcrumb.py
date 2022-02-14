from site_breadcrumb.serializers.site_breadcrumb import RetrieveSiteBreadcrumbModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveSiteBreadcrumbModelAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveSiteBreadcrumbModelSerializer
    