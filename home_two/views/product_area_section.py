from rest_framework.response import Response
from home_two.submodels.product_area_section import ProductAreaSectionModel
from home_two.serializers.product_area_section import RetrieveProductAreaSectionSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class RetrieveProductAreaSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveProductAreaSectionSerializer

    def _get_product_area_section_instance(self):
        product_area_section_instance = ProductAreaSectionModel.objects\
            .select_related('section_image',)\
            .order_by()\
            .only('heading', 'summary', 'section_image__image',
                  'section_image__caption',
                  ).first()

        return product_area_section_instance

    def get(self, request):
        product_area_section_instance = self._get_product_area_section_instance()

        product_area_section_instance_serializer = self._serializer_class(
            product_area_section_instance)

        return Response(product_area_section_instance_serializer.data)
