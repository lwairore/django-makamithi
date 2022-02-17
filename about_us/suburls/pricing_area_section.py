from about_us.views.pricing_area_section import RetrievePricingAreaSectionAPIView
from custom_utils.get_file_name_util import get_file_name
from django.urls import path

PRICING_AREA_SECTION_ROOT_ROUTE = 'retrieve/section/pricing-area/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_PRICING_AREA_SECTION_URL_ROUTE = ''

urlpatterns = [
    path(_RETRIEVE_PRICING_AREA_SECTION_URL_ROUTE,
         RetrievePricingAreaSectionAPIView.as_view()),
]
