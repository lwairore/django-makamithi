from custom_utils.pagination import CustomPagination, PaginationHandlerMixin
from contact_us.submodels.contact_info import ContactInfoModel
from contact_us.serializers.contact_info import RetrieveContactInfoModelSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView


class ListContactInfoAPIView(APIView, PaginationHandlerMixin):
    permission_classes = (AllowAny,)
    _serializer_class = RetrieveContactInfoModelSerializer
    pagination_class = CustomPagination

    def _list_contact_info_kueryset(self):
        contact_info_kueryset = ContactInfoModel.objects\
            .order_by()\
            .only('address_title',
                  'address',
                  'email',
                  'phone_number',)\
            .all()

        return contact_info_kueryset

    def get(self, request):
        contact_info_kueryset = self._list_contact_info_kueryset()

        results = self.paginate_queryset(contact_info_kueryset)

        contact_info_kueryset_serializer = self._serializer_class(
            contact_info_kueryset, many=True)

        return self.get_paginated_response(contact_info_kueryset_serializer.data)
