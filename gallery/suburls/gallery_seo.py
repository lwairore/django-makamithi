from django.urls import path
from gallery.views.gallery_seo import RetrieveGallerySEODetailsAPIView
from custom_utils.get_file_name_util import get_file_name


GALLERY_SEO_FOR_GALLERY_PAGE_ROOT_ROUTE = 'retrieve/seo/gallery/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_GALLERY_SEO_FOR_GALLERY_PAGE_URL_ROUTE = ''

urlpatterns = [
    # Seo for Gallery page
    path(
        _RETRIEVE_GALLERY_SEO_FOR_GALLERY_PAGE_URL_ROUTE,
        RetrieveGallerySEODetailsAPIView.as_view()
    ),
]
