from product.serializers.details_to_note_serializers import DetailToNoteSerializer
from custom_utils.iterable_object_is_not_empty import iterable_object_is_not_empty
from custom_utils.parse_json_data_util import parse_json_data
from custom_utils.string_is_not_empty import string_is_not_empty
from custom_utils.check_key_util import check_key
from django.db.models.query import Prefetch
from product.submodels.product import ProductModel
from product.submodels.rating_scale import ProductReviewModel
from product.serializers.product_review import ListProductReviewSerializer, UpdateProductReviewGatewaySerializer, UpdateProductReviewSerializer
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.status import HTTP_404_NOT_FOUND, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView


class ListUpdateProductReviewAPIView(APIView):
    permission_classes = (AllowAny,)

    def _get_product_instance(self, product_id: int):
        product_instance = None

        try:
            reviews_kueryset = ProductReviewModel.objects\
                .order_by()

            reviews_prefetch_related = Prefetch(
                'reviews', queryset=reviews_kueryset)

            product_instance = ProductModel.objects\
                .prefetch_related(reviews_prefetch_related).get(id=product_id)

            return product_instance

        except ProductModel.DoesNotExist as product_does_not_exist:
            raise product_does_not_exist

    def _list_reviews(self, product_instance: ProductModel):
        reviews = product_instance.reviews.order_by().all()

        return reviews

    def get(self, request, product_id: int):
        product_instance = None

        try:
            product_instance = self._get_product_instance(product_id)

        except ProductModel.DoesNotExist:
            return Response({'detail': f'Product with that id {product_id} not found.'}, status=HTTP_404_NOT_FOUND)

        reviews = self._list_reviews(product_instance)

        reviews_serializer = ListProductReviewSerializer(reviews, many=True)

        return Response(reviews_serializer.data)

    def post(self, request, product_id: int):
        product_instance = None

        try:
            product_instance = self._get_product_instance(product_id)

        except ProductModel.DoesNotExist:
            return Response({'detail': f'Product with that id {product_id} not found.'}, status=HTTP_404_NOT_FOUND)

        request_data = request.data

        if not check_key(request_data, 'reviews'):
            return Response({'detail': 'Nothing TODO here'})

        unformatted_reviews = request_data.get('reviews')

        print(unformatted_reviews)

        if not iterable_object_is_not_empty(unformatted_reviews):
            return Response({'detail': 'Nothing TODO here'})

        formatted_reviews = UpdateProductReviewSerializer()\
            .format_request_data(unformatted_reviews)

        if not iterable_object_is_not_empty(formatted_reviews):
            return Response({'detail': 'Nothing TODO here'})

        update_reviews_serializer = UpdateProductReviewGatewaySerializer(
            instance=product_instance,
            data={'reviews': formatted_reviews})

        if update_reviews_serializer.is_valid():
            details_to_note = update_reviews_serializer.save()

            print("details_to_note")
            print(details_to_note)

            if iterable_object_is_not_empty(details_to_note):
                details_to_note_serializer = DetailToNoteSerializer(
                    details_to_note)

                response_data = details_to_note_serializer.data

                return Response(response_data)
            else:
                return Response(data={})
        else:
            return Response(update_reviews_serializer.errors,
                            status=HTTP_400_BAD_REQUEST)
