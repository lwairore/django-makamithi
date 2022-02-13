from home_two.views.visit_now_cta_section import RetrieveVisitNowCtaSectionAPIView
from django.urls import path
from custom_utils.get_file_name_util import get_file_name

VISIT_NOW_CTA_SECTION_ROOT_ROUTE = 'retrieve/section/visit-now-cta/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_VISIT_NOW_CTA_SECTION_URL_ROUTE = ''

urlpatterns = [
    path(_RETRIEVE_VISIT_NOW_CTA_SECTION_URL_ROUTE,
         RetrieveVisitNowCtaSectionAPIView.as_view()),
]
