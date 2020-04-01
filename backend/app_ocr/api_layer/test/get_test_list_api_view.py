from app_ocr.app_layer.view_app_layer import AppListModelMixin
from app_ocr.api_layer.test.get_test_list_api_serializer import GetTestListSerializer
from app.utils.common.paginations.pagination import MyPagination
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from app_ocr import models

class GetTestListApi(AppListModelMixin):
    authentication_classes = ()  # 验证 authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = ()  # 权限 permission_classes = (permissions.IsAuthenticated,)
    pagination_class = MyPagination  # 分页
    queryset = models.OcrData.objects.all()
    serializer_class = GetTestListSerializer
    msg_list = "test ok"  # 提示信息



