from contact_us.views.work_with_us_cta_section import RetrieveWorkWithUsCtaSectionAPIView
from django.urls import path
from custom_utils.get_file_name_util import get_file_name

WORK_WITH_US_CTA_SECTION_ROOT_ROUTE = 'retrieve/section/work-with-us-cta/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_WORK_WITH_US_CTA_SECTION_URL_ROUTE = ''

urlpatterns = [
    path(_RETRIEVE_WORK_WITH_US_CTA_SECTION_URL_ROUTE,
         RetrieveWorkWithUsCtaSectionAPIView.as_view()),
]
