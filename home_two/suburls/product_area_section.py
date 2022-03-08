from home_two.views.product_area_section import RetrieveProductAreaSectionAPIView
from django.urls import path
from custom_utils.get_file_name_util import get_file_name


PRODUCT_AREA_SECTION_ROOT_ROUTE = 'retrieve/section/product-area/'

URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_RETRIEVE_PRODUCT_AREA_SECTION_URL_ROUTE = ''

urlpatterns = [
    path(_RETRIEVE_PRODUCT_AREA_SECTION_URL_ROUTE,
         RetrieveProductAreaSectionAPIView.as_view()),
]
