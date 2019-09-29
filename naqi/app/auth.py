from django.shortcuts import redirect

def check_login(func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('user'):
            return redirect('/login')
        return func(request, *args, **kwargs)
    return wrapper