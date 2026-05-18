from django.shortcuts import render, redirect
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        # 【修改这里】：处理完 POST 请求后，硬编码重定向到新 URL
        return redirect('/lists/the-new-page/')
    
    # 首页现在彻底清闲了，不需要查数据库，直接返回一个空模板即可
    return render(request, 'home.html')

# 【新增函数】：专门负责展示待办清单的新主厨
def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})
# lists/views.py 完整内容如下

from django.shortcuts import render, redirect
from lists.models import Item

def home_page(request):
    # 首页现在彻底变成了纯展示页面，啥也不用管了
    return render(request, 'home.html')

def view_list(request):
    # 专属展示页，负责查数据和渲染
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

# 【全新主厨】：专门负责处理新建清单的 POST 请求
def new_list(request):
    # 接收数据，存入数据库
    Item.objects.create(text=request.POST['item_text'])
    # 存完之后，把用户踢到那个假想的专属展示页
    return redirect('/lists/the-new-page/')