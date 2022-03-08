from gallery.suburls.gallery_detail_section import (
    GALLERY_DETAIL_SECTION_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as GALLERY_DETAIL_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)
from gallery.suburls.gallery import (
    GALLERY_SECTION_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION as GALLERY_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)
from gallery.suburls import URL_FILE_NAME
from gallery.apps import GalleryConfig
from gallery.suburls.gallery_seo import (GALLERY_SEO_FOR_GALLERY_PAGE_ROOT_ROUTE,
                                         URL_FILE_NAME_WITHOUT_EXTENSION as GALLERY_SEO_FOR_GALLERY_PAGE_URL_FILE_NAME_WITHOUT_EXTENSION)
from django.urls import path, include

app_name = GalleryConfig.name

_BASE_INCLUDE_PATH = '{}.{}.'.format(
    app_name,
    URL_FILE_NAME)

urlpatterns = [
    # Routes for Gallery
    path(
        GALLERY_SECTION_ROOT_ROUTE,
        include(
            _BASE_INCLUDE_PATH + GALLERY_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for section Gallery SEO
    path(GALLERY_SEO_FOR_GALLERY_PAGE_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH+GALLERY_SEO_FOR_GALLERY_PAGE_URL_FILE_NAME_WITHOUT_EXTENSION)),

    # Routes for section Gallery
    path(GALLERY_DETAIL_SECTION_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH+GALLERY_DETAIL_SECTION_URL_FILE_NAME_WITHOUT_EXTENSION)),
]
