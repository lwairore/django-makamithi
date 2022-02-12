from home_two.submodels.visit_now_cta_section import VisitNowCtaSectionModel
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class RetrieveVisitNowCtaSectionAPIView(APIView):
    permission_classes = (AllowAny,)

    def _get_visit_now_cta_section_instance(self):
        visit_now_cta_section_instance = VisitNowCtaSectionModel.objects\
            .select_related('background_image', 'section_image',)\
            .order_by()\
            .only('heading', 'description', 'section_image__image',
                  'section_image__caption',
                  'background_image__image',
                  'background_image__caption').first()

        return visit_now_cta_section_instance
