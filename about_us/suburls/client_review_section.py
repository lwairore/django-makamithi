from about_us.views.client_review_section import RetrieveClientReviewSectionAPIView
from custom_utils.get_file_name_util import get_file_name
from django.urls import path

CLIENT_REVIEW_SECTION_ROOT_ROUTE = 'retrieve/section/client-review/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_CLIENT_REVIEW_SECTION_URL_ROUTE = ''

urlpatterns = [
    path(_RETRIEVE_CLIENT_REVIEW_SECTION_URL_ROUTE,
         RetrieveClientReviewSectionAPIView.as_view()),
]
