"""naqi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.urls import path
from app.views import login, \
    index, user_add, nalist, \
    logout, delete_nalist, add_nalist, \
    user_list, user_delete, forbidden, \
    user_update

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', login),
    path('login', login),
    path('logout', logout),
    path('index', index),
    path('naList', nalist),
    path('naDelete', delete_nalist),
    path('naAdd', add_nalist),
    path('userList', user_list),
    path('userDelete', user_delete),
    path('userAdd', user_add),
    path('userUpdate', user_update),
    path('403', forbidden),
]
