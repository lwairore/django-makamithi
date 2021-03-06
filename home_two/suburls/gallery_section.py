from home_two.views.gallery_section import RetrieveGallerySectionAPIView
from django.urls import path
from custom_utils.get_file_name_util import get_file_name


GALLERY_SECTION_ROOT_ROUTE = 'retrieve/section/gallery/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_GALLERY_SECTION_URL_ROUTE = ''

urlpatterns = [
    path(_RETRIEVE_GALLERY_SECTION_URL_ROUTE,
         RetrieveGallerySectionAPIView.as_view()),
]
