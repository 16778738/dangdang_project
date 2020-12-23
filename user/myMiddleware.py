# _*_coding:UTF-8 _*_
# _*_coding:UTF-8 _*_
from django.shortcuts import render, redirect
from django.utils.deprecation import MiddlewareMixin


class MyMiddleware(MiddlewareMixin):  # 自定义的中间件
    def __init__(self, get_response):  # 初始化
        super().__init__(get_response)
        print("中间件已经初始化完毕")

    # view处理请求前执行
    def process_request(self, request):  # 某一个view
        if request.path == '/':
            return redirect('index:index')
        if request.path == '/indent/':
            is_login = request.session['login']
            if is_login:
                pass
            else:
                return render(request,'index/index.html')

# 在process_request之后View之前执行
def process_view(self, request, view_func, view_args, view_kwargs):
    print("view:", request, view_func, view_args, view_kwargs)


# view执行之后，响应之前执行
def process_response(self, request, response):
    print("response:", request, response)
    return response  # 必须返回response


# 如果View中抛出了异常
def process_exception(self, request, ex):  # View中出现异常时执行
    print("exception:", request, ex)
