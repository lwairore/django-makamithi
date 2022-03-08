from inbox.views.inbox import AddNewMessageAPIView
from django.urls import path
from custom_utils.get_file_name_util import get_file_name


LEAVE_A_MESSAGE_ROOT_ROUTE = 'leave-a-message/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_LEAVE_A_MESSAGE_URL_ROUTE = ''

urlpatterns = [
    # URLConf for Inbox
    path(
        _LEAVE_A_MESSAGE_URL_ROUTE,
        AddNewMessageAPIView.as_view()
    ),
]
