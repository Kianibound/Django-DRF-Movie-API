from rest_framework.pagination import CursorPagination, LimitOffsetPagination, PageNumberPagination

from movieAPP.models import WatchList


class WatchListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'size'
    max_page_size = 10
    last_page_strings = 'end'


class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 3
    max_limit = 10
    limit_query_param = 'limit'
    offset_query_param = 'start'
