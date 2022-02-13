from gallery.views.home_gallery import ListHomeGalleryAPIView
from django.urls.conf import path
from custom_utils.get_file_name_util import get_file_name


HOME_GALLERY_ROOT_ROUTE = 'list/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_LIST_GALLERY_URL_ROUTE = ''

urlpatterns = [
    path(_LIST_GALLERY_URL_ROUTE,
         ListHomeGalleryAPIView.as_view()),
]
