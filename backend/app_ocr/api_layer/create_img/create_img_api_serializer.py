# -*- coding: utf-8 -*-
"""
@Time ： 2020/4/2 02:05
@Auth ： Minhang
@File ：create_img_api_serializer.py
@IDE  ：PyCharm
"""
from app_ocr.app_layer.serializer_app_layer import AppSerializerApp
from rest_framework import serializers
from app_ocr import models
from app.utils.common.files.file import FileBase
from app.utils.common.exceptions import exception

class CreateImgSerializer(AppSerializerApp):
    ocr_img = serializers.SerializerMethodField(
        label="图片",
        required=False,
        allow_null=True,
    )
    ocr_key = serializers.SerializerMethodField(
        label="图片信息",
        required=False,
        allow_null=True,
    )

    class Meta:
        model = models.OcrData
        fields = ["ocr_img","ocr_key"]

    def get_ocr_img(self,obj):

        return 'data:image/jpeg;base64,%s' % obj.ocr_img

    def get_ocr_key(self,obj):

        return eval(obj.ocr_key)

    def create(self, validated_data):
        data = self.context["request"].data

        file = data.get("file", None) # 获取前端传过来的图片数据流
        # assert False
        if not file: # 图片为空
            raise exception.myException400({
                "success": False,
                "msg": "上传失败,后端没拿到图片",
                "results": "",
            })
        else: # 图片不为空
            base64_data = FileBase.image_to_base64(file)
            file_data = self.get_img_data_ocr(file)
            data_all = models.OcrData.objects.all()
            if data_all.count() >= 20: # 最大存20条数据
                models.OcrData.objects.all().delete()
            article_obj = models.OcrData.objects.create(
                ocr_img=base64_data,
                ocr_key=str(file_data),
            )

        return article_obj # 返回实例