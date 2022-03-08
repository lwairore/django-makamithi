from django.urls import path
from custom_utils.get_file_name_util import get_file_name
from partner.views.partner_area_section import RetrievePartnerAreaSectionAPIView

PARTNER_AREA_SECTION_ROOT_ROUTE = 'retrieve/section/partner-area/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_PARTNER_AREA_SECTION_URL_ROUTE = ''

urlpatterns = [
    path(
        _RETRIEVE_PARTNER_AREA_SECTION_URL_ROUTE,
        RetrievePartnerAreaSectionAPIView.as_view()
    )
]
