from service.models import VideoModel
from service.serializers.video import RetrieveVideoModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class RetrieveVideoAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveVideoModelSerializer

    def _get_video_instance(self):
        video_instance = VideoModel.objects\
            .only('thumbnail__image', 'thumbnail__caption',
                  'caption', 'video',
                  'title',)\
            .select_related('thumbnail')\
            .order_by()\
            .first()

        return video_instance

    def get(self, request):
        video_instance = self._get_video_instance()

        video_instance_serializer = self._serializer_class(
            video_instance)

        return Response(video_instance_serializer.data)
