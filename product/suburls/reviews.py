from custom_utils.get_file_name_util import get_file_name
from product.views.product_review import ListUpdateProductReviewAPIView
from django.urls import path

REVIEW_URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_LIST_PRODUCT_REVIEW_URL_ROUTE = 'list/product/'

urlpatterns = [
    path(_LIST_PRODUCT_REVIEW_URL_ROUTE, ListUpdateProductReviewAPIView.as_view()),
]
