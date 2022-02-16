from about_us.views.faq import ListFaqModelAPIView
from django.urls import path
from custom_utils.get_file_name_util import get_file_name


FAQ_ROOT_ROUTE = 'list/faq/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_LIST_FAQ_URL_ROUTE = ''

urlpatterns = [
    path(_LIST_FAQ_URL_ROUTE,
         ListFaqModelAPIView.as_view()),
]
