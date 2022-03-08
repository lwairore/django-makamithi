from header.views.header_section import RetrieveHeaderSectionForTopHeaderAPIView, RetrieveLogosForStickyHeaderSectionAPIView
from custom_utils.get_file_name_util import get_file_name
from django.urls import path

HEADER_SECTION_ROOT_ROUTE = ''

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_HEADER_SECTION_FOR_TOP_HEADER_URL_ROUTE = 'retrieve/section/top-header/'

_RETRIEVE_LOGOS_FOR_STICKY_HEADER_URL_ROUTE = 'retrieve/section/sticky-header/'

urlpatterns = [
    # 'URLConfs' for app 'Top header'
    path(_RETRIEVE_HEADER_SECTION_FOR_TOP_HEADER_URL_ROUTE,
         RetrieveHeaderSectionForTopHeaderAPIView.as_view()),

    #  'URLConf' for 'Sticky header'
    path(_RETRIEVE_LOGOS_FOR_STICKY_HEADER_URL_ROUTE,
         RetrieveLogosForStickyHeaderSectionAPIView.as_view()),
]
