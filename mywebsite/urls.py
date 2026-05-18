from django.contrib import admin
from django.urls import path
from lists import views  # 引入我们自己写的 views

urlpatterns = [
    # path('admin/', admin.site.urls), # 这一行注释掉或者留着都没关系
    path('', views.home_page, name='home'),
    path('lists/new', views.new_list, name='new_list'),
    # 【新增这一行】：配置属于那个新页面的专属路由
    path('lists/the-new-page/', views.view_list, name='view_list'),
]