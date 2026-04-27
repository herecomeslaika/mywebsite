from django.db import models

class Item(models.Model):
    # 给模型增加一个 text 属性，类型是“文本类型”，默认值为空字符串
    text = models.TextField(default='')