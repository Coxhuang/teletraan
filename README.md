[TOC]

# Teletraan backend

## #1 使用

1. GitHub地址

[https://github.com/Coxhuang/teletraan](https://github.com/Coxhuang/teletraan)


2. Teletraan backend 地址

👉👉👉 [http://admin.minhung.me:20420/#/](http://admin.minhung.me:20420/#/)

3. 演示

![](https://raw.githubusercontent.com/Coxhuang/yosoro/master/20200402092234.png)


## #2 环境

- 后端 


```
CentOS6.8
Python3.7.6
Django2.0.7
djangorestframework3.8.2
pytesseract0.3.3
```

- 前端

```
"vue": "^2.5.2",
"axios": "^0.19.0",
"vue-axios": "^2.1.4",
"vue-router": "^3.0.1",
"vuex": "^3.1.1",
"view-design": "^4.0.0"
```

## #3 Api文档 

**简要描述：** 

- 提取图片信息

**请求URL：** 
- ` http://api.minhung.me:20421/api/app_ocr/create-img/ `
  
**请求方式：**
- POST 

**参数：** 

|参数名|必选|类型|说明|
|:----    |:---|:----- |-----   |
|file |是  |file |图片流   |

 **返回示例**
``` 
{
    "success":true,
    "msg":"ok",
    "results":
    {
        "ocr_img":"图片base64",
        "ocr_key":["1234","5678"]
    }
}
```
 **返回参数说明** 

|参数名|类型|说明|
|:-----  |:-----|-----                           |
|success |bool   |接口成功状态码  |
|msg |str   |返回消息  |
|results |dict   |返回结果  |
|results["ocr_img] |str   |上传图片的base64 |
|results["ocr_key] |list   |图片提取到的信息, |

 **备注** 

- 使用该接口时,前端需要以图片的文件流形式传入

## #4 设计思路

1. 前端上传一张带有字母的图片
2. 后端拿到图片后,通过pytesseract提取出图片中的信息
3. 后端将图片中的信息以及图片返回给前端并渲染









