from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class PaginationHandlerMixin(object):
    @property
    def paginator(self):
        """
        The paginator instance associated with the view, or `None`.
        """
        if not hasattr(self, '_paginator'):
            if self.pagination_class is None:
                self._paginator = None
            else:
                self._paginator = self.pagination_class()
        else:
            pass
        return self._paginator

    def paginate_queryset(self, queryset):
        """
         Return a single page of results, or `None` if pagination is disabled.
         """
        if self.paginator is None:
            return None
        return self.paginator.paginate_queryset(queryset,
                                                self.request,
                                                view=self)

    def get_paginated_response(self, data):
        """
         Return a paginated style `Response` object for the given output data.
        """
        assert self.paginator is not None
        return self.paginator.get_paginated_response(data)


class CustomPagination(PageNumberPagination):
    page_size = 6
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'p'

    def get_paginated_response(self, data):
        response = {
            'results': data,
            'count': self.page.paginator.count
            
        }

        if self.page.has_next():
            next_page_number = self.page.next_page_number()

            response['next'] = next_page_number

        return Response(response)
