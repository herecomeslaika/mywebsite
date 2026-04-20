from django.test import TestCase

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        # 1. 使用 Django 内置的模拟客户端，像真人一样去访问首页
        response = self.client.get('/')
        
        # 2. 一键断言：检查这个响应是不是使用了名叫 'home.html' 的模板渲染出来的
        self.assertTemplateUsed(response, 'home.html')