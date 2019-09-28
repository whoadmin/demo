from django.shortcuts import render, redirect
from utils.encrypt import decrypt_data, SHA256
import base64
from .models import Account
# Create your views here.

def login(request):
    error_msg = ''
    if request.method == "POST":
        username = request.POST.get('username', None)
        passwd = request.POST.get('passwd', None)
        passwd = base64.b64decode(passwd)
        passwd = decrypt_data(passwd)
        passwd = SHA256(passwd)
        res = Account.objects.filter(username=username, password=passwd)
        if res.count() >= 1:
            return redirect('/index')
        else:
            error_msg = '用户名密码不正确'
    pub_key = open('./pub.pem').read()
    return render(request, 'login.html', {'key': pub_key, 'errmsg': error_msg})

def index(request):
    return render(request, 'index.html')