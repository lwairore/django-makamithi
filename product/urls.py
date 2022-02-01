from product.views.product import ListProductAPIView
from product.views.category import ListProductCategoryAPIView
from django.urls.conf import path

urlpatterns = [
    path('list/category/', ListProductCategoryAPIView.as_view()),
    path('list/product/', ListProductAPIView.as_view()),
]
