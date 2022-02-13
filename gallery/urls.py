from gallery.suburls import URL_FILE_NAME
from gallery.apps import GalleryConfig
from gallery.suburls.home_gallery import HOME_GALLERY_ROOT_ROUTE
from django.urls.conf import path, include

app_name = GalleryConfig.name

_BASE_INCLUDE_PATH = '{}.{}.'.format(
    app_name,
    URL_FILE_NAME)

urlpatterns = []
