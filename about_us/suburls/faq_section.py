from about_us.views.faq_section import RetrieveFaqSectionAPIView
from custom_utils.get_file_name_util import get_file_name
from django.urls import path

FAQ_SECTION_ROOT_ROUTE = 'retrieve/section/faq/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_FAQ_SECTION_URL_ROUTE = ''

urlpatterns = [
    path(_RETRIEVE_FAQ_SECTION_URL_ROUTE,
         RetrieveFaqSectionAPIView.as_view()),
]
