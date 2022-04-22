from rest_framework.pagination import PageNumberPagination

class Pagination(PageNumberPagination):
    page_size = 10  # 每页显示记录数，前端没有传入page_num，则默认显示此参数
    page_size_query_param = 'page_num'  # 前端传入每页显示条数
    page_query_param = "page"  # 前端传入第几页
    max_page_size = 100  # 后端控制每页显示最大记录数