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
from app_ocr import models

class CreateImgApi(AppCreateModeMixin):

    authentication_classes = ()  # 验证 authentication_classes = (JSONWebTokenAuthentication,)
    permission_classes = ()  # 权限 permission_classes = (permissions.IsAuthenticated,)
    throttle_scope = 'throttle_3_Min'  # 节流每分钟3次
    queryset = models.OcrData.objects.all()
    serializer_class = CreateImgSerializer
    msg_create = "ok"  # 提示信息

