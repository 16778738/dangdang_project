import time
import uuid
import datetime

from django.db import transaction
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from user.models import TCar, TBook, TUser, TOrder, TAddress, TOrderItem


# Create your views here.


# 面向对象实现购物车,方法:添加,删除,修改,查询
class Book:
    def __init__(self, id, count):
        book = TBook.objects.get(pk=id)
        self.id = id
        self.count = count
        self.new_price = book.new_price
        self.picture = book.picture
        self.book_name = book.book_name

    def totalprice(self):
        return round(float(self.new_price) * float(self.count), 2)


class Car:
    def __init__(self):
        self.book_list = []  # 空列表
        self.index = 0

    def add_book(self, id, count=1):
        book = self.get_book(id)  # 查询bookid是否存在
        if book:
            book.count = int(book.count) + int(count)  # 存在直接修改数量
        else:  # 不存在创建book对象存放
            book = Book(id=id, count=count)
            self.book_list.append(book)

    # 根据id查询某本书是否存在购物车
    def get_book(self, id):
        for book in self.book_list:
            if book.id == id:
                return book

    # 根据id删除
    def remove_book(self, id):
        book = self.get_book(id)
        self.book_list.remove(book)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index < len(self.book_list):
            item = self.book_list[self.index]
            self.index += 1
            return item
        else:
            raise StopIteration

    def __len__(self):
        return len(self.book_list)


def rem_book(request):
    book_id = request.GET.get("id")  # 书的id
    car = request.session.get('car')
    # 判断是否有登录状态
    user_name = request.COOKIES.get('txtUsername')
    user_pwd = request.COOKIES.get('txtPassword')
    req = TUser.objects.filter(user_name=user_name, user_pwd=user_pwd)
    if req:
        id = TUser.objects.get(user_name=user_name)  # 用户id
        try:
            with transaction.atomic():
                car = TCar.objects.filter(user_id=id)  # 用户的购物车
                book_item = TCar.objects.get(book_id=book_id)  # 需要删除的book对象
                print(book_item)
                book_item.delete()
                sum_price = 0
                for i in car:
                    sum_price += round(float(i.book.new_price) * float(i.count), 2)
                    return JsonResponse({"error": 0, "msg": "删除成功", "sum_price": sum_price})
                return JsonResponse({"error": 1, "msg": "删除失败"})
        except Exception as e:
            print(e)
            return JsonResponse({"error": 1, "msg": "删除失败"})
    else:
        if car:
            totalprice = 0
            sum_price = 0
            for i in car:
                totalprice = round(float(i.new_price) * float(i.count), 2)
                sum_price += round(float(i.new_price) * float(i.count), 2)
            with transaction.atomic():
                car.remove_book(book_id)
            request.session['car'] = car
            return JsonResponse({"error": 0, "msg": "删除成功", "sum_price": sum_price, "totalprice": totalprice})
        return JsonResponse({"error": 1, "msg": "删除失败"})


def add_car(request):
    book_id = request.GET.get("bookid")
    book_num = request.GET.get("booknum")
    book_num1 = request.GET.get("booknum1")  # 数量失焦的返回值
    user_name = request.COOKIES.get('txtUsername')
    user_pwd = request.COOKIES.get('txtPassword')
    car = request.session.get('car')  # 存放的未登陆的car
    # 判断是否有登录状态
    req = TUser.objects.filter(user_name=user_name, user_pwd=user_pwd)
    sum_price = 0
    totalprice = 0
    if req:
        id = TUser.objects.get(user_name=user_name)  # 用户id
        car = TCar.objects.filter(user_id=id)  # 用户的购物车
        if car:
            # 判断book是否存在
            book_item = TCar.objects.filter(book_id=book_id)
            if book_item:  # 存在book
                if book_num1:  # 失焦直接赋值给count
                    book_item[0].count = int(book_num1)
                    book_item[0].save()
                    totalprice = book_item[0].totalprice()
                else:
                    book_item[0].count += int(book_num)
                    book_item[0].save()
            else:
                with transaction.atomic():
                    TCar.objects.create(book_id=book_id, count=book_num, user_id=id.id)
        else:
            with transaction.atomic():
                TCar.objects.create(book_id=book_id, count=book_num, user_id=id.id)
        for i in car:
            sum_price += round(float(i.book.new_price) * float(i.count), 2)
        return JsonResponse({"msg": "添加购物车成功!快去看看吧!", "error": 0, "totalprice": totalprice, "sum_price": sum_price})
    else:
        if car:
            pass
        else:
            car = Car()
        car.add_book(book_id, int(book_num))
        request.session['car'] = car
        sum_price = 0  # 总计
        totalprice = 0  # 小计
        for book in car.book_list:
            if int(book.id) == int(book_id):
                totalprice = round(float(book.new_price) * float(book.count), 2)
            sum_price += round(float(book.new_price) * float(book.count), 2)
        return JsonResponse({"msg": "添加购物车成功!快去看看吧!", "error": 0, "sum_price": sum_price, "totalprice": totalprice})


def car(request):
    # 判断是否有登录状态
    user_name = request.COOKIES.get('txtUsername')
    user_pwd = request.COOKIES.get('txtPassword')
    req = TUser.objects.filter(user_name=user_name, user_pwd=user_pwd)
    car = request.session.get('car')  # 存放的未登陆的car
    if req:
        request.session['login'] = 'ok'
        # 将session中的数据迁移到购物车表中，相同数据应该合并数量，同时还需要清空session
        try:
            with transaction.atomic():
                id = TUser.objects.get(user_name=user_name)  # 用户id
                if car:
                    # 判断book是否存在
                    for i in car:
                        book_item = TCar.objects.filter(book_id=i.id)
                        if book_item:
                            book_item[0].count += int(i.count)
                            book_item[0].save()
                            print(i.id, i.count)
                        else:
                            with transaction.atomic():
                                TCar.objects.create(book_id=i.id, count=i.count, user_id=id.id)
                    request.session.flush()
                else:
                    with transaction.atomic():
                        car = TCar.objects.filter(user_id=id)
                    sum_price = 0  # 总计
                    for i in car:
                        sum_price += round(float(i.book.new_price) * float(i.count), 2)
            return render(request, 'car/car.html',
                          {"car": car, "sum_price": sum_price, "user_name": user_name})
        except Exception as e:
            print(e)
    else:
        if car:
            totalprice = 0
            sum_price = 0  # 总计
            for i in car:
                totalprice = round(float(i.new_price) * float(i.count), 2)
                sum_price += round(float(i.new_price) * float(i.count), 2)
            return render(request, 'car/car.html',
                          {"car": car, "totalprice": totalprice, "sum_price": sum_price, })
    return render(request, 'car/car.html')


def order(request):
    # 判断是否有登录状态
    user_name = request.COOKIES.get('txtUsername')
    user_pwd = request.COOKIES.get('txtPassword')
    req = TUser.objects.filter(user_name=user_name, user_pwd=user_pwd)
    sum_price = 0
    if req:
        id = TUser.objects.get(user_name=user_name)  # 用户id
        car = TCar.objects.filter(user_id=id)
        with transaction.atomic():
            address = TAddress.objects.filter(user_id=id)
        for i in car:
            sum_price += round(float(i.book.new_price) * float(i.count), 2)
        return render(request, "car/indent.html",
                      {"address": address, "car": car, "sum_price": sum_price, "user_name": user_name})
    return redirect("user:login")


def order_ok(request):
    user_name = request.COOKIES.get('txtUsername')
    id = TUser.objects.get(user_name=user_name)  # 用户id
    car = TCar.objects.filter(user_id=id)  # 用户的car
    sum_price = 0  # 总计
    # 获取到提交订单的地址
    address = request.GET.get("address")
    address_id = TAddress.objects.filter(address=address)[0]
    # 生成订单号
    order_id = str(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))) + str(time.time()).replace('.', '')[-7:]
    create_time = datetime.datetime.now().strftime('%Y-%m-%d')
    # 订单项
    for i in car:
        sum_price += round(float(i.book.new_price) * float(i.count), 2)
    with transaction.atomic():
        order = TOrder.objects.create(order_id=order_id, create_time=create_time, price=sum_price,
                                      address_id=address_id.id,
                                      user_id=id.id)

    count = 0
    for i in car:
        with transaction.atomic():
            order_item = TOrderItem.objects.create(count=i.count, book_id=i.id, order_id=order.id)
        count += i.count
        i.delete()
    return render(request, 'car/indent ok.html',
                  {"user_name": user_name, "order": order, "count": count, "order_item": order_item,
                   "address": address_id})


def order_submit(request):
    user_name = request.COOKIES.get('txtUsername')
    id = TUser.objects.get(user_name=user_name)  # 用户
    t_address = TAddress.objects.filter(user_id=id)  # 用户的地址

    ship_man = request.POST.get("ship_man")
    address = request.POST.get("address")
    addr_mobile = request.POST.get("addr_mobile")
    cellphone = request.POST.get("cellphone")
    post = request.POST.get("post")

    print(ship_man, address, addr_mobile, cellphone, post)
    # 判断地址是否存在,不存在添加
    if t_address[0].address == address:
        return JsonResponse({"msg": "地址已经存在", "error": 1})
    else:
        TAddress.objects.create(address=address, name=ship_man, post_code=post, cellphone=cellphone,
                                addr_mobile=addr_mobile,
                                user_id=id.id)
    return JsonResponse({"msg": "订单生成", "error": 0})
