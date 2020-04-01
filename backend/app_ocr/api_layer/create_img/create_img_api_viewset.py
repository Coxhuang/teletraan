# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/2 02:04
@Auth ： Minhang
@File ：create_img_api_viewset.py
@IDE  ：PyCharm
"""
from app_ocr.app_layer.view_app_layer import AppCreateModeMixin
from app_ocr.api_layer.create_img.create_img_api_serializer import CreateImgSerializer
from rest_framework import permissions
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from app_ocr import models

class CreateImgApi(AppCreateModeMixin):
    authentication_classes = ()  # 验证 authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = ()  # 权限 permission_classes = (permissions.IsAuthenticated,)
    queryset = models.OcrData.objects.all()
    serializer_class = CreateImgSerializer
    msg_create = "ok"  # 提示信息

    # def create(self, request, *args, **kwargs):
    #
    #     serializer = self.get_serializer(data=request.data)
    #     self.validation_error(serializer=serializer)  # 自定义Serializer异常处理
    #     # serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     # headers = self.get_success_headers(serializer.data)
    #
    #     data = serializer.data if self.results_display else None #
    #     print("data:",data)
    #     return Response({
    #         "success": True,
    #         "msg": self.msg_create,
    #         "results": data
    #     }, status=status.HTTP_201_CREATED)
