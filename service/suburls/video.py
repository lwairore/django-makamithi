from django.urls import path
from custom_utils.get_file_name_util import get_file_name
from service.views.video import RetrieveVideoAPIView

VIDEO_ROOT_ROUTE = 'retrieve/section/video-area/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_VIDEO_URL_ROUTE = ''

urlpatterns = [
    path(
        _RETRIEVE_VIDEO_URL_ROUTE,
        RetrieveVideoAPIView.as_view()
    )
]
