from django.core.paginator import Paginator
from django.shortcuts import render
from user.models import TBook, TCategory, TUser


# Create your views here.

def booklist(request):
    cate1 = request.GET.get("cate1")  # 获取一级标签的id
    cate2 = request.GET.get("cate2")  # 获取二级标签的id
    cates1 = TCategory.objects.filter(level=1)  # 一级标签
    cates2 = TCategory.objects.filter(level=2)  # 二级标签
    # #根据标签id获取其model对象
    # title1 = TCategory.objects.filter(pk=cate1)
    # title2 = TCategory.objects.filter(pk=cate2)[0]
    # print(title2.category_id,6545645645646)
    if cate1 and cate1 != 'None':
        # 获取到属于一级标题下二级标题的所有书籍
        paginator = Paginator(TBook.objects.filter(category__parent_id=cate1), per_page=3)
    else:
        paginator = Paginator(TBook.objects.filter(category_id=cate2), per_page=3)
    # 实现分页
    num = request.GET.get("num", 1)
    page = paginator.page(num)
    # 通过cookice判断是否免登陆状态
    user_name = request.COOKIES.get('txtUsername')
    user_pwd = request.COOKIES.get('txtPassword')
    res = TUser.objects.filter(user_name=user_name, user_pwd=user_pwd)
    if res:
        return render(request, 'book/booklist.html', {"user_name":user_name,"cates1": cates1, "cates2": cates2,"page": page,"cate1":cate1,"cate2":cate2})
    return render(request, 'book/booklist.html', {"cates1": cates1, "cates2": cates2,"page": page,"cate1":cate1,"cate2":cate2})


def bookdetails(request):
    id = request.GET.get("id")  # 获取前端返回的图书id
    book = TBook.objects.filter(pk=id)[0]  # 根据id查询到书的信息
    # discount 折扣计算返回给前端
    discount = round((book.new_price / book.old_price * 10), 2)
    # 通过cookice判断是否免登陆状态
    user_name = request.COOKIES.get('txtUsername')
    user_pwd = request.COOKIES.get('txtPassword')
    res = TUser.objects.filter(user_name=user_name, user_pwd=user_pwd)
    if res:
        return render(request, 'book/bookdetails.html', {"user_name":user_name,"book": book, "discount": discount})
    return render(request, 'book/bookdetails.html', {"book": book, "discount": discount})
