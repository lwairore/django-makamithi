from product.views.category import ListProductCategoryAPIView
from django.urls.conf import path

urlpatterns = [
    path('list/category/', ListProductCategoryAPIView.as_view()),
]
