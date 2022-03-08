from inbox.suburls.inbox import (LEAVE_A_MESSAGE_ROOT_ROUTE,
                                 URL_FILE_NAME_WITHOUT_EXTENSION as LEAVE_A_MESSAGE_URL_FILE_NAME_WITHOUT_EXTENSION)
from inbox.suburls import URL_FILE_NAME
from inbox.apps import InboxConfig
from django.urls import include, path

app_name = InboxConfig.name

_BASE_INCLUDE_PATH = '{}.{}.'.format(
    app_name,
    URL_FILE_NAME)

urlpatterns = [
    # Routes for Leave a Message
    path(
        LEAVE_A_MESSAGE_ROOT_ROUTE,
        include(
            _BASE_INCLUDE_PATH + LEAVE_A_MESSAGE_URL_FILE_NAME_WITHOUT_EXTENSION)),
]
