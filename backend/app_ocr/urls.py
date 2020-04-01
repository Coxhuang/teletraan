from django.urls import path
from django.urls import include
from rest_framework import routers

from app_ocr.api_layer.test.get_test_list_api_view import GetTestListApi
from app_ocr.api_layer.create_img.create_img_api_viewset import CreateImgApi

GetTestListApiRouter = routers.DefaultRouter()
GetTestListApiRouter.register('', GetTestListApi,base_name="")
CreateImgApiRouter = routers.DefaultRouter()
CreateImgApiRouter.register('', CreateImgApi,base_name="")

urlpatterns = [
    path('get-test-list/', include(GetTestListApiRouter.urls)),
    path('create-img/', include(CreateImgApiRouter.urls)),
]
