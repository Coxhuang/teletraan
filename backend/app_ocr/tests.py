from django.test import TestCase

# Create your tests here.
# 首先安装两个包
# pip install pytesseract
# pip install Pillow

from PIL import Image
import pytesseract

# 指定图片路径和识别的语言
text = pytesseract.image_to_string(Image.open('/Users/coxhuang/Desktop/1.png'), lang='chi_sim')
print(text)