from django.contrib import admin

# Register your models here.

from foodorder.models import userinfo

from foodorder.models import foodmenu

from foodorder.models import orderhist

admin.site.register(userinfo)

admin.site.register(foodmenu)

admin.site.register(orderhist)

