from service.suburls import URL_FILE_NAME
from service.suburls.service import LIST_SERVICE_ROOT_ROUTE, URL_FILE_NAME_WITHOUT_EXTENSION
from service.apps import ServiceConfig
from django.urls.conf import path, include

app_name = ServiceConfig.name

_BASE_INCLUDE_PATH = '{app_name}.{URL_FILE_NAME}.{FILE_NAME_WITHOUT_EXTENSION}'\
    .format(
        app_name=app_name,
        URL_FILE_NAME=URL_FILE_NAME)

urlpatterns = [
    # Routes for showing list of services
    path(LIST_SERVICE_ROOT_ROUTE,
         include(
             _BASE_INCLUDE_PATH.format(
                 FILE_NAME_WITHOUT_EXTENSION=URL_FILE_NAME_WITHOUT_EXTENSION)
         ))
]
