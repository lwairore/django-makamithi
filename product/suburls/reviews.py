from custom_utils.get_file_name_util import get_file_name
from product.views.product_review import ListUpdateProductReviewAPIView
from django.urls import path

REVIEW_URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_LIST_PRODUCT_REVIEW_URL_ROUTE = ''

_ADD_PRODUCT_REVIEW_URL_ROUTE = 'add/'

urlpatterns = [
    # List reviews for a particular product
    path(_LIST_PRODUCT_REVIEW_URL_ROUTE,
         ListUpdateProductReviewAPIView.as_view()),

    # Add review for a product
    path(_ADD_PRODUCT_REVIEW_URL_ROUTE, ListUpdateProductReviewAPIView.as_view()),
]
