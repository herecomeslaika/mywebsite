from django.shortcuts import render

def home_page(request):
    # 尝试从请求的 POST 数据中获取名为 'item_text' 的内容
    # 如果没获取到（比如第一次正常访问网页时），就默认是一个空字符串 ''
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })