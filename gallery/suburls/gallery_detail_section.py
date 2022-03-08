from gallery.views.gallery_detail_section import RetrieveGalleryDetailSectionAPIView
from custom_utils.get_file_name_util import get_file_name
from django.urls import path

GALLERY_DETAIL_SECTION_ROOT_ROUTE = 'retrieve/section/gallery-detail/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_GALLERY_DETAIL_SECTION_URL_ROUTE = ''

urlpatterns = [
    path(_RETRIEVE_GALLERY_DETAIL_SECTION_URL_ROUTE,
         RetrieveGalleryDetailSectionAPIView.as_view()),
]
