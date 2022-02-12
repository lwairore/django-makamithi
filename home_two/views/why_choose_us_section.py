from home_two.submodels import why_choose_us_section
from home_two.serializers.why_choose_us_section import RetrieveWhyChooseUsSectionSerializer
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView


class RetrieveWhyChooseUsSectionAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveWhyChooseUsSectionSerializer

    def _get_why_choose_us_section_instance(self):
        why_choose_us_section_instance = why_choose_us_section.WhyChooseUsSectionModel.objects\
            .select_related('section_image',)\
            .order_by()\
            .only('heading', 'description', 'section_image__image',
                  'section_image__caption',).first()

        return why_choose_us_section_instance
