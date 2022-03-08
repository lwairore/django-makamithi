from contact_us.views.leave_us_a_message_section import RetrieveLeaveUsAMessageSectionAPIView
from custom_utils.get_file_name_util import get_file_name
from django.urls import path

LEAVE_US_A_MESSAGE_SECTION_ROOT_ROUTE = 'retrieve/section/leave-us-a-message/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_LEAVE_US_A_MESSAGE_SECTION_URL_ROUTE = ''

urlpatterns = [
    path(_RETRIEVE_LEAVE_US_A_MESSAGE_SECTION_URL_ROUTE,
         RetrieveLeaveUsAMessageSectionAPIView.as_view()),
]
