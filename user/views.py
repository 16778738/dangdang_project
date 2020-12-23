import random, string, traceback
from django.db import transaction
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from captcha.image import ImageCaptcha
from user.models import TUser


# Create your views here.
def regist(request):
    url = request.GET.get('url')
    print(url)
    return render(request, 'user/register.html', {"url": url})


def login(request):
    # 判断是否有登录状态
    user_name = request.COOKIES.get('txtUsername')
    user_pwd = request.COOKIES.get('txtPassword')
    url = request.GET.get('url')
    print(url, 22222)
    if url == None:
        url = "http://127.0.0.1:8000/index/"
    req = TUser.objects.filter(user_name=user_name, user_pwd=user_pwd)
    if req:
        request.session['login'] = 'ok'
        return render(request, 'user/login.html', {"txtUsername": user_name, "txtPassword": user_pwd, 'url': url})
    return render(request, 'user/login.html')


def regist_ok(request):
    url = request.GET.get('url')
    print(url)
    txt_username = request.GET.get("txt_username")
    return render(request, 'user/register ok.html', {"txt_username": txt_username, "url": url})


# 生成验证码
def getCaptcha(request):
    # 生成img对象
    img = ImageCaptcha()
    code = random.sample(string.ascii_uppercase + string.ascii_lowercase + string.digits, 4)
    # 拼接字符,通过session传递验证码
    random_code = ''.join(code)
    request.session['code'] = random_code
    # 生成验证码图片
    data = img.generate(random_code)
    return HttpResponse(data, 'image/png')


# 验证码校验
def check_code(request):
    txt_vcode = request.POST.get("txt_vcode")  # 验证码
    code = request.session['code']
    print(code)
    if code.lower() == txt_vcode.lower():
        return JsonResponse({"msg": "验证码正确", "error": 0})
    return JsonResponse({"msg": "验证码错误", "error": 1})


def regist_logic(request):
    url = request.GET.get('url')
    print(url)
    txt_username = request.POST.get("txt_username")
    txt_password = request.POST.get("txt_password")
    txt_repassword = request.POST.get("txt_repassword")
    txt_vcode = request.POST.get("txt_vcode")  # 验证码
    chb_agreement = request.POST.get("chb_agreement")  # 霸王条款
    code = request.session['code']
    try:
        with transaction.atomic():
            if txt_username == '' or txt_password == '' or txt_repassword == '' or txt_vcode == '':
                10 / 0
            if code.lower() == txt_vcode.lower():
                res = TUser.objects.filter(user_name=txt_username)
                if res:
                    return JsonResponse({"msg": "用户已存在", "error": 0})
                elif txt_password == txt_repassword:
                    resp = JsonResponse({"msg": "创建成功", "error": 1, "url": url})
                    TUser.objects.create(user_name=txt_username, user_pwd=txt_password)
                    resp.set_cookie('txtUsername', txt_username, max_age=7 * 24 * 3600)
                    resp.set_cookie('txtPassword', txt_password, max_age=7 * 24 * 3600)
                    return resp
                else:
                    return JsonResponse({"msg": "两次密码不一致", "error": 2})
            return JsonResponse({"msg": "验证码错误", "error": 3})
    except Exception as e:
        traceback.print_exc()
        print(e)
        return JsonResponse({"msg": "输入数据非法", "error": 4})


# 检查用户名
def check_username(request):
    txtUsername = request.GET.get("txtUsername")
    print(txtUsername, "检查用户名是否存在")
    res = TUser.objects.filter(user_name=txtUsername)
    if res:
        return JsonResponse({"msg": "用户名存在", "error": 0})
    return JsonResponse({"msg": "该用户名不存在请检查!", "error": 1})


def login_logic(request):
    txtUsername = request.POST.get("txtUsername")
    txtPassword = request.POST.get("txtPassword")
    txtVerifyCode = request.POST.get("txtVerifyCode")
    code = request.session['code']
    url = request.GET.get('url')
    autologin = request.POST.get("autologin")  # 是否勾选免登录
    try:
        if txtUsername == '' or txtPassword == '' or txtVerifyCode == '':
            10 / 0
        if code.lower() == txtVerifyCode.lower():
            res = TUser.objects.filter(user_name=txtUsername, user_pwd=txtPassword)
            if res:
                request.session['login'] = 'ok'
                resp = JsonResponse({"msg": "登陆成功!", "error": 0, "url": url})
                if autologin:
                    resp.set_cookie('txtUsername', txtUsername, max_age=7 * 24 * 3600)
                    resp.set_cookie('txtPassword', txtPassword, max_age=7 * 24 * 3600)
                return resp
            else:
                return JsonResponse({"msg": "用户名或密码错误!", "error": 1})
        else:
            return JsonResponse({"msg": "验证码错误", "erro": 2})
    except Exception as e:
        print(e)
        traceback.print_exc()
        return JsonResponse({"msg": "请输入有效数据", "error": 3})


# 退出登陆状态,删除session
def exit(request):
    username = request.GET.get("username")  # 获取到需要退出的用户名
    request.session.flush()
    resp = JsonResponse({"msg": "退出成功!", "error": 0})
    resp.delete_cookie('txtUsername')
    resp.delete_cookie('txtPassword')
    if username:
        return resp
    else:
        return JsonResponse({"msg": "发生错误!", "error": 1})
