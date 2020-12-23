from datetime import datetime, timedelta
from django.shortcuts import render
from user.models import TCategory, TBook, TUser


# Create your views here.
def index(request):
    time = datetime.now().date() - timedelta(days=3650)  # 获取当前时间的上一个时间
    cate1 = TCategory.objects.filter(level=1)  # 一级标签
    cate2 = TCategory.objects.filter(level=2)  # 二级标签
    booklist1 = TBook.objects.order_by("-publish_time")[:10]  # 根据上架时间排名
    booklist2 = TBook.objects.filter(publish_time__gte=time).order_by("-sales")  # 根据最新上架时间,销售排名

    # 通过cookice判断是否免登陆状态
    user_name = request.COOKIES.get('txtUsername')
    user_pwd = request.COOKIES.get('txtPassword')
    res = TUser.objects.filter(user_name=user_name, user_pwd=user_pwd)
    if res:
        return render(request, 'index/index.html',
                      {"user_name": user_name, "cates1": cate1, "cates2": cate2, "booklist1": booklist1,
                       "booklist2": booklist2, })
    return render(request, 'index/index.html',
                  {"cates1": cate1, "cates2": cate2, "booklist1": booklist1, "booklist2": booklist2})
