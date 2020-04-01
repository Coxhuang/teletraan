from django.db import models

class OcrData(models.Model):

    ocr_img = models.TextField(
        verbose_name="base64",
        default="",
    )
    ocr_key = models.TextField(
        verbose_name="图片中的关键字",
        default=""
    )

