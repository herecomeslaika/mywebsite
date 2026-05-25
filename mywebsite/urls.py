from django.contrib import admin
from django.urls import path, re_path  # 【注意】：这里新增了 re_path 的导入
from lists import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('lists/new', views.new_list, name='new_list'),
    re_path(r'^lists/(\d+)/$', views.view_list, name='view_list'),
    # 【新增下面这行】：专门处理追加事项的请求
    re_path(r'^lists/(\d+)/add_item$', views.add_item, name='add_item'),
]