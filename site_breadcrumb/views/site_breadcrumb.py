from site_breadcrumb.submodels.site_breadcrumb import SiteBreadcrumbModel
from site_breadcrumb.serializers.site_breadcrumb import RetrieveSiteBreadcrumbModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveSiteBreadcrumbModelAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveSiteBreadcrumbModelSerializer

    def _get_site_breadcrumb_instance(self):
        site_breadcrumb_instance = SiteBreadcrumbModel.objects\
            .only(
                'background_image__image', 'background_image__caption',)\
            .select_related('background_image')\
            .order_by().first()

        return site_breadcrumb_instance
