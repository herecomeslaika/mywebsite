from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    # 这是一个全新的测试方法
    def test_home_page_return_correct_html(self):
        # 1. 模拟网络请求
        request = HttpRequest()  
        
        # 2. 把请求交给我们的视图函数处理，并拿到它的响应结果
        response = home_page(request)  
        
        # 3. 把响应内容解码成我们可以看懂的字符串（HTML 代码）
        html = response.content.decode('utf8')  
        
        # 4. 断言：网页必须以 <html> 标签开头
        self.assertTrue(html.startswith('<html>'))  
        
        # 5. 断言：网页的标题必须包含 "To-Do lists"
        self.assertIn('<title>To-Do lists</title>', html)  
        
        # 6. 断言：网页必须以 </html> 标签结尾
        self.assertTrue(html.endswith('</html>'))