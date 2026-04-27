from django.test import TestCase
from lists.models import Item
class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    # 新增的测试方法：专门测试 POST 请求
    def test_can_save_a_POST_request(self):
        # 1. 模拟发送一个 POST 请求，假装用户在输入框提交了 'A new list item'
        response = self.client.post('/', data={'item_text': 'A new list item'})
        
        # 2. 检查网页的 HTML 源码中，是否包含了我们刚刚提交的那句话
        self.assertIn('A new list item', response.content.decode())
class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first list item')
        self.assertEqual(second_saved_item.text, 'Item the second')