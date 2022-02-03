from custom_utils.get_file_name_util import get_file_name
from product.views.product_review import ListProductReviewAPIView
from django.urls import path

REVIEW_URL_FILE_NAME_WITHOUT_EXTENSION = get_file_name(__file__)

_PRODUCT_ID_PARAMETER = '<int:product_id>'

_LIST_PRODUCT_REVIEW_URL_ROUTE = 'list/product/' + _PRODUCT_ID_PARAMETER + '/'

urlpatterns = [
    path('list/product/<int:product_id>/', ListProductReviewAPIView.as_view()),
]
