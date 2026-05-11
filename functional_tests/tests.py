from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.webdriver.common.by import By
import time  # 确保导入了 time
from selenium.common.exceptions import WebDriverException # 导入这个异常

MAX_WAIT = 10 # 告诉测试，最多容忍等 10 秒
class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    # 这是我们新提取的“辅助工具”
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:  # 开启无限循环
            try:
                table = self.browser.find_element(By.ID, 'id_list_table')
                rows = table.find_elements(By.TAG_NAME, 'tr')
                self.assertIn(row_text, [row.text for row in rows])
                return  # 如果上面都没报错，说明找到了！立刻退出循环，一毫秒都不多等。
            except (AssertionError, WebDriverException) as e:
                # 如果没找到（抛出了异常），就看看是不是等得太久了
                if time.time() - start_time > MAX_WAIT:
                    raise e  # 如果超过了 10 秒，说明真的出 Bug 了，把异常抛出去让测试失败
                time.sleep(0.5)  # 如果还没超时，就稍微睡 0.5 秒，然后再试一次

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 张三听说有一个在线待办事项的应用
        self.browser.get(self.live_server_url)
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element(By.TAG_NAME, 'h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

 # 他输入了“Buy flowers”并按回车
        inputbox.send_keys('Buy flowers')
        inputbox.send_keys(Keys.ENTER)
        # 删掉了 time.sleep(1)
        self.wait_for_row_in_list_table('1: Buy flowers') # 用了新方法

        # 他又输入了“Give a gift to Lisi”并按回车
        inputbox = self.browser.find_element(By.ID, 'id_new_item')
        inputbox.send_keys('Give a gift to Lisi')
        inputbox.send_keys(Keys.ENTER)
        # 删掉了 time.sleep(1)
        self.wait_for_row_in_list_table('1: Buy flowers') # 用了新方法
        self.wait_for_row_in_list_table('2: Give a gift to Lisi') # 用了新方法

        self.fail('Finish the test!')

