from django.test import TestCase
from lists.models import Item  # 确保导入了 Item 模型

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')



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
class ListViewTest(TestCase):

    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        # 【注意这里】：请求的是新 URL，而不是首页 '/'
        response = self.client.get('/lists/the-new-page/')

        # assertContains 是个好东西，它能同时检查状态码 200 和页面内容
        self.assertContains(response, 'itemey 1')
        self.assertContains(response, 'itemey 2')
    def test_uses_list_template(self):
        response = self.client.get('/lists/the-new-page/')
        self.assertTemplateUsed(response, 'list.html')
class NewListTest(TestCase):

    def test_can_save_a_POST_request(self):
        # 注意：这里的目标 URL 变成了 /lists/new
        self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

    def test_redirects_after_POST(self):
        response = self.client.post('/lists/new', data={'item_text': 'A new list item'})
        # 使用 Django 的超强快捷断言，一行顶过去两行
        self.assertRedirects(response, '/lists/the-new-page/')