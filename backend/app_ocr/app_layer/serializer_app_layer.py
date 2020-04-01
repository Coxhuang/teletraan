from app.utils.common.mixins.serializers_mixin import MySerializerMixin
from PIL import Image
import pytesseract


# *******************************************************************************
# *                                                                             *
# * @标题  : APP-app序列化
# * @功能  : app下自定义序列化方法
# * @备注  : None
# *                                                                             *
# *******************************************************************************
class AppSerializerApp(MySerializerMixin):

    def get_img_data_ocr(self, file) -> list:
        """
        获取图片中的信息
        :param file: 图片文件流
        :return: 图片信息 (List)
        """

        text = pytesseract.image_to_string(Image.open(file), lang='chi_sim')
        ret_list = []
        for foo in text.split("\n"):
            for fo in foo.split(" "):
                if fo:
                    ret_list.append(fo)
        print(ret_list)
        return ret_list