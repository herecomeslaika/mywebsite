from django.test import TestCase
from lists.models import Item, List  # 确保导入了 Item 和 List 模型

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')



    def test_saving_and_retrieving_items(self):
        # 1. 先创建一个父清单，并保存到数据库
        list_user = List()
        list_user.save()

        # 2. 创建第一个 Item，并把它挂到这个清单上
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_user  # 关键修复：指定所属清单
        first_item.save()

        # 3. 创建第二个 Item，同样挂上去
        second_item = Item()
        second_item.text = 'Item the second'
        second_item.list = list_user # 关键修复：指定所属清单
        second_item.save()

        # 4. 验证清单是否正确保存
        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_user)

        # 5. 验证待办事项是否正确保存，并且属于刚才的清单
        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, list_user) # 验证归属
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, list_user) # 验证归属
class ListViewTest(TestCase):

    def test_displays_all_list_items(self):
        # 1. 先创建一个父清单
        list_user = List.objects.create()
        # 2. 创建 Item 时，必须带上 list=list_user 这个参数！
        Item.objects.create(text='itemey 1', list=list_user)
        Item.objects.create(text='itemey 2', list=list_user)

        response = self.client.get('/lists/the-new-page/')

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