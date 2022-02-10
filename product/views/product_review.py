# from product.serializers.details_to_note_serializers import DetailToNoteSerializer
# from custom_utils.iterable_object_is_not_empty import iterable_object_is_not_empty
# from custom_utils.parse_json_data_util import parse_json_data
# from custom_utils.string_is_not_empty import string_is_not_empty
# from custom_utils.check_key_util import check_key
# from django.db.models.query import Prefetch, QuerySet
# from product.submodels.product import ProductModel
# from product.submodels.rating_scale import ProductReviewModel
# from product.serializers.product_review import RetrieveProductReviewSerializer, UpdateProductReviewGatewaySerializer, UpdateProductReviewSerializer
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
# from rest_framework.status import HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
# from rest_framework.views import APIView


# class RetrieveDeleteProductAPIView(APIView):
#     permission_classes = (AllowAny,)

#     def _get_product_instance(self, product_id: int):
#         product_instance = None

#         try:
#             reviews_kueryset = ProductReviewModel.objects\
#                 .only('id').order_by()

#             reviews_prefetch_related = Prefetch(
#                 'reviews', queryset=reviews_kueryset)

#             product_instance = ProductModel.objects\
#                 .prefetch_related(reviews_prefetch_related).get(id=product_id)

#             return product_instance

#         except ProductModel.DoesNotExist as product_does_not_exist:
#             raise product_does_not_exist

#     def _get_product_review_instance(self, product_instance: ProductModel, product_review_id: int,
#                                      return_instance_as_kueryset=False):

#         product_review_kueryset: QuerySet = product_instance.reviews\
#             .filter(id=product_review_id)

#         if not product_review_kueryset.exists():
#             raise ProductReviewModel.DoesNotExist

#         return product_review_kueryset if return_instance_as_kueryset else product_review_kueryset.first()

#     def get(self, request, product_id: int, product_review_id: int):
#         product_instance = None

#         try:
#             product_instance = self._get_product_instance(product_id)

#         except ProductModel.DoesNotExist:
#             return Response({'detail': f'Product with that id {product_id} not found.'}, status=HTTP_404_NOT_FOUND)

#         product_review_instance = None

#         try:
#             product_review_instance = self._get_product_review_instance(
#                 product_instance, product_review_id)
#         except ProductReviewModel.DoesNotExist:
#             return Response({'detail': f'Product review with that id {product_review_id} not found.'}, status=HTTP_404_NOT_FOUND)

#         product_review_serializer = RetrieveProductReviewSerializer(
#             product_review_instance)

#         return Response(product_review_serializer.data)

#     def delete(self, request, product_id: int, product_review_id: int):
#         product_instance = None

#         try:
#             product_instance = self._get_product_instance(product_id)

#         except ProductModel.DoesNotExist:
#             return Response({'detail': f'Product with that id {product_id} not found.'}, status=HTTP_404_NOT_FOUND)

#         product_review_kueryset = None

#         try:
#             product_review_kueryset = self._get_product_review_instance(
#                 product_instance=product_instance, product_review_id=product_review_id,
#                 return_instance_as_kueryset=True)
#         except ProductReviewModel.DoesNotExist:
#             return Response({'detail': f'Product review with that id {product_review_id} not found.'}, status=HTTP_404_NOT_FOUND)

#         product_review_kueryset.delete()

#         return Response(status=HTTP_204_NO_CONTENT)


# class ListUpdateProductReviewAPIView(APIView):
#     permission_classes = (AllowAny,)

#     def _get_product_instance(self, product_id: int):
#         product_instance = None

#         try:
#             reviews_kueryset = ProductReviewModel.objects\
#                 .order_by()

#             reviews_prefetch_related = Prefetch(
#                 'reviews', queryset=reviews_kueryset)

#             product_instance = ProductModel.objects\
#                 .prefetch_related(reviews_prefetch_related).get(id=product_id)

#             return product_instance

#         except ProductModel.DoesNotExist as product_does_not_exist:
#             raise product_does_not_exist

#     def _list_reviews(self, product_instance: ProductModel):
#         reviews = product_instance.reviews.order_by().all()

#         return reviews

#     def get(self, request, product_id: int):
#         product_instance = None

#         try:
#             product_instance = self._get_product_instance(product_id)

#         except ProductModel.DoesNotExist:
#             return Response({'detail': f'Product with that id {product_id} not found.'}, status=HTTP_404_NOT_FOUND)

#         reviews = self._list_reviews(product_instance)

#         reviews_serializer = RetrieveProductReviewSerializer(
#             reviews, many=True)

#         return Response(reviews_serializer.data)

#     def post(self, request, product_id: int):
#         product_instance = None

#         try:
#             product_instance = self._get_product_instance(product_id)

#         except ProductModel.DoesNotExist:
#             return Response({'detail': f'Product with that id {product_id} not found.'}, status=HTTP_404_NOT_FOUND)

#         request_data = request.data

#         if not check_key(request_data, 'reviews'):
#             return Response({'detail': 'Nothing TODO here'})

#         unformatted_reviews = request_data.get('reviews')

#         print(unformatted_reviews)

#         if not iterable_object_is_not_empty(unformatted_reviews):
#             return Response({'detail': 'Nothing TODO here'})

#         formatted_reviews = UpdateProductReviewSerializer()\
#             .format_request_data(unformatted_reviews)

#         if not iterable_object_is_not_empty(formatted_reviews):
#             return Response({'detail': 'Nothing TODO here'})

#         update_reviews_serializer = UpdateProductReviewGatewaySerializer(
#             instance=product_instance,
#             data={'reviews': formatted_reviews})

#         if update_reviews_serializer.is_valid():
#             details_to_note = update_reviews_serializer.save()

#             print("details_to_note")
#             print(details_to_note)

#             if iterable_object_is_not_empty(details_to_note):
#                 details_to_note_serializer = DetailToNoteSerializer(
#                     details_to_note)

#                 response_data = details_to_note_serializer.data

#                 return Response(response_data)
#             else:
#                 return Response(data={})
#         else:
#             return Response(update_reviews_serializer.errors,
#                             status=HTTP_400_BAD_REQUEST)
