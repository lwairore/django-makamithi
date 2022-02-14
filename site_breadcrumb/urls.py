from site_breadcrumb.suburls import URL_FILE_NAME
from django.conf.urls import include
from site_breadcrumb.suburls.site_breadcrumb import (SITE_BREADCRUMB_ROOT_ROUTE,
                                                     URL_FILE_NAME_WITHOUT_EXTENSION as SITE_BREADCRUMB_URL_FILE_NAME_WITHOUT_EXTENSION)
from django.urls import path
from site_breadcrumb.apps import SiteBreadcrumbConfig


app_name = SiteBreadcrumbConfig.name

_BASE_INCLUDE_PATH = '{}.{}.'.format(
    app_name,
    URL_FILE_NAME)

urlpatterns = [
    # Routes for Site-Breadcrumb
    path(SITE_BREADCRUMB_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH + SITE_BREADCRUMB_URL_FILE_NAME_WITHOUT_EXTENSION
         ))
]
