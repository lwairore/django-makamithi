from product.suburls.reviews import REVIEW_URL_FILE_NAME_WITHOUT_EXTENSION
from product.suburls import URL_FILE_NAME
from product.apps import ProductConfig
from product.views.product import ListProductAPIView
from product.views.category import ListProductCategoryAPIView
from django.urls.conf import path, include

urlpatterns = [
    path('list/category/', ListProductCategoryAPIView.as_view()),
    path('list/product/', ListProductAPIView.as_view()),
    path('reviews/',
         include(f'{ProductConfig.name}.{URL_FILE_NAME}.{REVIEW_URL_FILE_NAME_WITHOUT_EXTENSION}')),

]
