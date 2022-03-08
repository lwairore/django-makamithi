from home_two.views.badge import ListBadgeAPIView
from django.urls import path
from custom_utils.get_file_name_util import get_file_name


BADGE_ROOT_ROUTE = 'list/badge/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_LIST_BADGE_URL_ROUTE = ''

urlpatterns = [
    path(_LIST_BADGE_URL_ROUTE,
         ListBadgeAPIView.as_view()),
]
