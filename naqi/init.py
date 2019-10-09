from utils.encrypt import SHA256
import time
import django
import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'naqi.settings'
django.setup()
from app.models import Account

def init():
    t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    Account.objects.create(
        nickname='admin',
        username='admin',
        password=SHA256(b'admin'),
        create_time=t,
        perm_id=1
    )

init()