from gallery.views.gallery import ListGalleryForGalleryPageAPIView, RetrieveGalleryDetailAPIView
from gallery.views.home_gallery import ListGalleryForHomePageAPIView
from django.urls import path
from custom_utils.get_file_name_util import get_file_name


GALLERY_SECTION_ROOT_ROUTE = ''

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_LIST_GALLERY_FOR_HOME_PAGE_URL_ROUTE = 'list/section/home/'

_LIST_GALLERY_FOR_GALLERY_PAGE_URL_ROUTE = 'list/section/gallery/'

_GALLERY_ID_ROUTE_PARAMETER = '<int:gallery_id>'

_RETRIEVE_GALLERY_DETAIL_ROUTE = f'{_GALLERY_ID_ROUTE_PARAMETER}/details/'


urlpatterns = [
    # List gallery for home page
    path(_LIST_GALLERY_FOR_HOME_PAGE_URL_ROUTE,
         ListGalleryForHomePageAPIView.as_view()),

    #  List gallery for gallery page
    path(_LIST_GALLERY_FOR_GALLERY_PAGE_URL_ROUTE,
         ListGalleryForGalleryPageAPIView.as_view()),

    #     Retrieve Gallery details
    path(_RETRIEVE_GALLERY_DETAIL_ROUTE,
         RetrieveGalleryDetailAPIView.as_view()),
]
