from about_us.models import FaqModel
from about_us.serializers.faq import RetrieveFaqModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class ListFaqModelAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveFaqModelSerializer

    def _list_faq_kueryset(self):
        faq_kueryset = FaqModel.objects\
            .order_by()\
            .only('question', 'answer',)\
            .all()

        return faq_kueryset

    def get(self, request):
        faq_kueryset = self._list_faq_kueryset()

        faq_kueryset_serializer = self._serializer_class(
            faq_kueryset, many=True)

        return Response(faq_kueryset_serializer.data)
