from django.utils.deprecation import MiddlewareMixin

# *******************************************************************************
# *                                                                             *
# * @标题  : 系统中间件
# * @功能  : 系统中间件
# * @备注  : None
# *                                                                             *
# *******************************************************************************
class MySystemMiddleware(MiddlewareMixin):  # 继承Middlewaremixin
    pass
    # def process_exception(self, request, exceptions):
    #     print(request)
    #     print(exceptions,type(exceptions))
    #     raise exception.myException401("oooo")

    # def process_response(self, request, response):
    #     print(response)
    #
    #     return response

    # def process_request(self, request):
    #     print("This is process_request : ", request.user)
    #
    #     return None

    # def process_view(self, request, callback, callback_args, callback_kwargs):
    #     print("This is process_view : ", request.user)




