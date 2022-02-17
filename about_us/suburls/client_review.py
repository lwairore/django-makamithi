from custom_utils.get_file_name_util import get_file_name
from about_us.views.client_review import ListClientReviewModelAPIView
from django.urls import path

CLIENT_REVIEW_ROOT_ROUTE = 'list/client-review/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_LIST_CLIENT_REVIEW_URL_ROUTE = ''

urlpatterns = [
    path(_LIST_CLIENT_REVIEW_URL_ROUTE,
         ListClientReviewModelAPIView.as_view()),
]
