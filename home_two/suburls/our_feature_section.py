from home_two.views.our_feature_section import RetrieveFeatureSectionAPIView
from django.urls import path
from custom_utils.get_file_name_util import get_file_name


FEATURE_SECTION_ROOT_ROUTE = 'retrieve/feature-section/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_FEATURE_SECTION_URL_ROUTE = ''

urlpatterns = [
    path(_RETRIEVE_FEATURE_SECTION_URL_ROUTE,
         RetrieveFeatureSectionAPIView.as_view()),
]
