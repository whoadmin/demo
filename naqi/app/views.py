from django.shortcuts import render, redirect, HttpResponse
from utils.encrypt import decrypt_data, SHA256
import base64
from .models import Account, Nac, Perm
from .auth import check_login
from django.core.paginator import Paginator, EmptyPage
from django.http.response import JsonResponse
import time
# Create your views here.

def login(request):
    error_msg = ''
    if request.method == "POST":
        username = request.POST.get('username', None)
        passwd = request.POST.get('passwd', None)
        passwd = base64.b64decode(passwd)
        passwd = decrypt_data(passwd)
        passwd = SHA256(passwd)
        res = Account.objects.filter(
            username=username,
            password=passwd
        )
        if res.count() >= 1:
            account = res.get()
            request.session['user'] = account.username
            return redirect('/index')
        else:
            error_msg = '用户名密码不正确'
    pub_key = open('./pub.pem').read()
    return render(request, 'login.html', {'key': pub_key, 'errmsg': error_msg})

def logout(request):
    request.session['user'] = None
    return redirect('/login')

@check_login
def index(request):
    return redirect('/naList')

@check_login
def nalist(request):
    q = request.GET.get('query', None)
    t = request.GET.get('type', None)
    nac = None
    try:
        if q == None:
            nac = Nac.objects.all().order_by('update_time')
        if t == None:
            nac = Nac.objects.all().order_by('update_time')
        elif t == 'hid':
            nac = Nac.objects.filter(hostid=q).order_by('update_time')
        elif t == 'ip':
            nac = Nac.objects.filter(ip=q).order_by('update_time')
        elif t == 'email':
            nac = Nac.objects.filter(ad_mail=q).order_by('update_time')
        elif t == 'name':
            nac = Nac.objects.filter(ad_name=q).order_by('update_time')
        paginator = Paginator(nac, 25)
        page = request.GET.get('page', 1)
        u = request.session['user']
        data = paginator.page(page)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    except Exception:
        data = paginator.page(1)
    ret = {
        'data': data,
        'page_range': paginator.page_range,
        'u': u
    }
    return render(request, 'na-list.html', ret)

@check_login
def delete_nalist(request):
    data = {
        'code': 1,
        'msg': 'failed',
        'ret': None,
    }
    if request.method == "POST":
        id = request.POST.get('id', None)
        if id != None:
            res = Nac.objects.get(id=id).delete()
            if res:
                data['code'] = 0
                data['msg'] = 'success'
                data['ret'] = res
    return JsonResponse(data)

@check_login
def add_nalist(request):
    return render(request, 'na-add.html')

@check_login
def user_list(request):
    users = Account.objects.all().order_by('create_time')
    try:
        paginator = Paginator(users, 25)
        page = request.GET.get('page', 1)
        u = request.session['user']
        data = paginator.page(page)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    except Exception:
        data = paginator.page(1)
    perm = []
    for u in users:
        p = Perm.objects.get(id=u.perm_id)
        perm.append(p)
    ret = {
        'data': data,
        'page_range': paginator.page_range,
        'u': u,
        'perm': perm
    }
    return render(request, 'user-list.html', ret)

@check_login
def user_delete(request):
    data = {
        'code': 1,
        'msg': 'failed',
        'ret': None,
    }
    if request.method == "POST":
        id = request.POST.get('id', None)
        if id != None:
            res = Account.objects.get(id=id).delete()
            if res:
                data['code'] = 0
                data['msg'] = 'success'
                data['ret'] = res
    return JsonResponse(data)

def create_user(request):
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    a = Account.objects.create(
        username='admin',
        password=SHA256(b'admin'),
        nickname='admin',
        create_time=t,
        perm_id=1
    )
    # print(SHA256(b'admin'))
    return HttpResponse('create success')

