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