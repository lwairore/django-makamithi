from home_two.views.why_choose_us_section import RetrieveWhyChooseUsSectionAPIView
from custom_utils.get_file_name_util import get_file_name
from django.urls import path

WHY_CHOOSE_US_SECTION_ROOT_ROUTE = 'retrieve/why-choose-us-section/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_WHY_CHOOSE_US_SECTION_URL_ROUTE = ''

urlpatterns = [
    path(_RETRIEVE_WHY_CHOOSE_US_SECTION_URL_ROUTE,
         RetrieveWhyChooseUsSectionAPIView.as_view()),
]
