from home_two.views.counter_area_section import RetrieveCounterAreaSectionAPIView
from custom_utils.get_file_name_util import get_file_name
from django.urls import path

COUNTER_AREA_SECTION_ROOT_ROUTE = 'retrieve/section/counter-area/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_COUNTER_AREA_SECTION_URL_ROUTE = ''

urlpatterns = [
    path(_RETRIEVE_COUNTER_AREA_SECTION_URL_ROUTE,
         RetrieveCounterAreaSectionAPIView.as_view()),
]
