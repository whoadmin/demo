from django.shortcuts import render, redirect, HttpResponse
from utils.encrypt import decrypt_data, SHA256
import base64
from .models import Account, Nac
from .auth import check_login
from django.core.paginator import Paginator, EmptyPage
from django.http.response import JsonResponse
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
    return redirect('/list')

@check_login
def search(request):
    q = request.GET.get('query', None)
    t = request.GET.get('type', 'hid')
    if t == 'hid':
        pass
    elif t == 'ip':
        pass
    elif t == 'email':
        pass
    elif t == '':
        pass
    return

@check_login
def nalist(request):
    nac = Nac.objects.all().order_by('update_time')
    paginator = Paginator(nac, 25)
    page = request.GET.get('page', 1)
    u = request.session['user']
    try:
        data = paginator.page(page)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    except Exception:
        data = paginator.page(1)
    return render(request, 'na-list.html', {'data': data, 'page_range': paginator.page_range, 'u': u})

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
def create_user(request):
    Account.objects.create(
        username='admin',
        password=SHA256(b'admin'),
        privilege=1
    )
    return HttpResponse('create success')

