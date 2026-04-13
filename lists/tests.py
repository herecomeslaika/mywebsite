from django.test import TestCase
from django.urls import resolve
from lists.views import home_page  # (1) 注意这里：改成了从 lists 应用导入

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')  # (2)
        self.assertEqual(found.func, home_page)  # (3)
