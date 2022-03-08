from footer.views.contact_info import ListContactInfoAPIView
from custom_utils.get_file_name_util import get_file_name
from django.urls import path

CONTACT_INFO_ROOT_ROUTE = 'retrieve/contact-info/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)


_RETRIEVE_CONTACT_INFO_URL_ROUTE = ''

urlpatterns = [
    #  'URLConf' for 'Contact info section'
    path(_RETRIEVE_CONTACT_INFO_URL_ROUTE,
         ListContactInfoAPIView.as_view()),
]
