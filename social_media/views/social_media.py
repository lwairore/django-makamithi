from social_media.submodels.social_media import SocialMediaModel
from social_media.serializers.social_media import RetrieveSocialMediaSerializer
from django.db.models.query import QuerySet
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response


class ListSocialMediaAPIView(APIView):
    permission_classes = (AllowAny, )
    _serializer_class = RetrieveSocialMediaSerializer

    def _list_social_media_kueryset(self) -> QuerySet:
        social_media_kueryset = SocialMediaModel.objects.only(
            'link', 'title', 'icon',)\
            .order_by()\
            .all()

        return social_media_kueryset

    def get(self, request):
        social_media_kueryset = self._list_social_media_kueryset()

        social_media_kueryset_serializer = self._serializer_class(
            social_media_kueryset, many=True)

        return Response(social_media_kueryset_serializer.data)
