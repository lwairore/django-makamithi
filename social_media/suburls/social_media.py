from social_media.views.social_media import ListSocialMediaAPIView
from django.urls import path
from custom_utils.get_file_name_util import get_file_name


SOCIAL_MEDIA_ROOT_ROUTE = ''

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_LIST_SOCIAL_MEDIA_URL_ROUTE = 'list/'


urlpatterns = [
    # List gallery for Social Media
    path(_LIST_SOCIAL_MEDIA_URL_ROUTE,
         ListSocialMediaAPIView.as_view()),

]
