from gallery.submodels.gallery import GalleryModel
from gallery.serializers.gallery import RetrieveGalleryDetailModelSerializer, RetrieveGalleryModelForGalleryPageSerializer
from custom_utils.pagination import CustomPagination, PaginationHandlerMixin
from django.db.models.query import QuerySet
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework.response import Response


class RetrieveGalleryDetailAPIView(APIView):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveGalleryDetailModelSerializer

    def _retrieve_gallery_instance(self, gallery_id: int) -> GalleryModel:
        gallery_instance = None

        try:
            gallery_instance = GalleryModel.objects\
                .only('title', 'keywords', 'layout_image__image', 'layout_image__caption',
                      'occured_on', 'created_at', 'modified_date', 'description',)\
                .select_related('layout_image',)\
                .get(id=gallery_id)
        except GalleryModel.DoesNotExist as gallery_does_not_exist:
            raise gallery_does_not_exist

        return gallery_instance

    def get(self, request, gallery_id: int):
        gallery_instance = None

        try:
            gallery_instance = self._retrieve_gallery_instance(
                gallery_id)
        except GalleryModel.DoesNotExist:
            return Response(
                data={
                    'error': f'Gallery with id {gallery_id} does not exist'},
                status=HTTP_404_NOT_FOUND)

        gallery_instance_serializer = self._serializer_class(gallery_instance)

        return Response(gallery_instance_serializer.data)


class ListGalleryForGalleryPageAPIView(APIView, PaginationHandlerMixin):
    permission_classes = (AllowAny, )
    _serializer_class = RetrieveGalleryModelForGalleryPageSerializer
    pagination_class = CustomPagination

    def _list_gallery_kueryset(self) -> QuerySet:
        gallery_kueryset = GalleryModel.objects.only(
            'id', 'gallery_preview__image', 'gallery_preview__caption',
            'category__title', 'title',)\
            .order_by()\
            .select_related('gallery_preview', 'category', )\
            .all()

        return gallery_kueryset

    def get(self, request):
        gallery_kueryset = self._list_gallery_kueryset()

        results = self.paginate_queryset(gallery_kueryset)

        gallery_kueryset_serializer = self._serializer_class(
            results, many=True)

        return self.get_paginated_response(gallery_kueryset_serializer.data)
