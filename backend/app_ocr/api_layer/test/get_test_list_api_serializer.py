from app_ocr.app_layer.serializer_app_layer import AppSerializerApp
from rest_framework import serializers
from app_ocr import models

class GetTestListSerializer(AppSerializerApp):

    class Meta:
        model = models.OcrData
        fields = ["ocr_img","ocr_key",]
