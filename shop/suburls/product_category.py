from shop.views.product_category import ListProductCategoryAPIView
from django.urls import path
from custom_utils.get_file_name_util import get_file_name


URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_LIST_PRODUCT_CATEGORY_ROUTE = 'list/'

PRODUCT_CATEGORY_ROOT_ROUTE = 'product-category/'


urlpatterns = [
    path(_LIST_PRODUCT_CATEGORY_ROUTE, ListProductCategoryAPIView.as_view()),
]
