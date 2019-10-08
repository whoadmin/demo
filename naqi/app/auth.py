from django.shortcuts import redirect
from app.models import Account

def check_login(func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('user'):
            return redirect('/login')
        return func(request, *args, **kwargs)
    return wrapper

def check_perm(user):
    a = Account.objects.filter(username=user).get()
    if a.perm_id == 1:
        return True
    else:
        return False