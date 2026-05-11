from django.shortcuts import render, redirect
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    # 去数据库里把所有的 Item 都查出来，放到一个叫 items 的变量里
    items = Item.objects.all()
    
    # 把 items 打包成字典，传给 home.html
    return render(request, 'home.html', {'items': items})