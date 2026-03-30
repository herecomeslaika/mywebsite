from selenium import webdriver

# 1. 启动一个具体的浏览器实例（这里以 Chrome 为例）
browser = webdriver.Chrome()

# 2. 输入网址，确保这里所有的标点符号（包括冒号和斜杠）都是英文状态
browser.get('http://localhost:8000')
assert 'Django' in browser.page_source
