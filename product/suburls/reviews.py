from product.views.product_review import ListProductReviewAPIView
from django.urls import path

urlpatterns = [
    path('list/product/<int:product_id>/', ListProductReviewAPIView.as_view()),
]
